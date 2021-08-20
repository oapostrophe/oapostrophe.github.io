---
layout: post
title:  "Clear and Conspicuous: a browser extension that counteracts UI Dark Patterns"
author: sean
categories: [ Privacy, User Interface, Dark Patterns, CCPA ]
image: assets/images/ccpa1/ccpa-link.png
featured: false
hidden: false
description: "Blog post overviewing the development of a browser extension countering UI Dark Patterns in CCPA data sale opt-outs."
comments: false
---

*How I built a browser extension to combat UI Dark Patterns in CCPA opt-out links*

## The problem

What do Best Buy, Hulu, and CNN have in common? It's hard to see, but for California residents, there's a new link on their homepage, along with 35.8% of other top US websites.

The California Consumer Privacy Act (CCPA), which began enforcement July 2020, mandates that websites which sell users' information post a link titled "Do Not Sell My Personal Information" allowing them to opt out. CCPA requires that such links be "clear and conspicuous"; however, [my summery 2020 research](https://oapostrophe.github.io/ccpa-study/) revealed that most are anything but.  Most of these links are in small font, placed in an inconspicuous location buried within a list of rarely-visited page sections like "Terms and Conditions" and "Legal Information."  Users often have to scroll, sometimes a great distance, to the bottom of the page in order to even see these links.  This makes them hard to spot and unlikely to be used—on an experimental website, I found that just **1%** of users interacted with this style of link design.

![A typical CCPA Link]({{site.baseurl}}/assets/images/ccpa1/ccpa-link.png)

*A typical CCPA Link: far from clear and conspicuous.  Notice how far down the page is scrolled.*

I wanted to know: could a browser extension help correct course for CCPA?  What if someone could see the web the way CCPA intended, with a truly "clear and conspicuous" notification when their information is being sold?  While these links are difficult to see for humans, their legally-mandated standard phrasing could make them easy to detect programmatically.  Over the course of Fall 2020, I set out to build such an extension.

## Designing a Solution

The first step was to design an automated method for detecting CCPA links.  During my previous research, I had examined these links across the Top 500 US websites.  While legally, they are only supposed to say "Do Not Sell My Personal Information", I found 12 different variations in link titling.  I looked for a common phrase that could detect all these variations while remaining specific enough to not often occur in other contexts.  Together, the phrases "Do Not Sell" and "Don't Sell" appeared in every link title, and when manually searching the top 500 US sites for these phrases, I never had either of them match a page element other than a CCPA link.  These phrases obviously do occur in other contexts, but any more specificity in search phrasing would miss a substantial portion of links.  Thus, I decided that they together hit the optimal balance of precision and recall.

I considered how to search for these phrases, and whether any sort of specific page area or element type could be targeted for search.  But the wide range of websites that the extension needs to work on have very different link placement and page designs, without any clear universal pattern.  For example, while most links are contained in an `<a>` tag, I found some pages with different designs, such as using javascript to link the opt out when clicked.  Ultimately, I decided that it was more important this extension be reliable than extremely fast, as users will count on it to detect when their information is being sold.  Thus, I planned to implement a linear search of every page element for the target phrases, which I later found in testing never took more than a couple of seconds (and frequently was much faster).

The next step was to decide what should actually be done when the link is found.  I wanted to transform these hidden links into visible, clear, and usable notifications.  My research had found that banner notifications were far more effective in making users aware they have a right to opt out of information sale, as well as substantially more likely to be utilized.  Thus, I decided to notify the user when a link was found by injecting a banner overlaying the page.  Of course, a notification that's not actionable is of limited use.  So I also planned to include some way of accessing the page's opt out directly in the injected banner.

![The banner used in our study]({{site.baseurl}}/assets/images/whos-selling-my-info1/study-banner.png)

*The banner design which users utilized at the highest rate in my prior research.*

When designing the banner, I based it on the design which got the highest rate of user opt-out in my study: a notification with a single option reading "Do Not Sell My Personal Information".  Contrary to real CCPA notices, I wrote my notice to be as short as possible with plain and direct language.  I also included a link to more information in case the user needs more background on what the notification means.  I picked a red background for the design, which [another study](https://dl.acm.org/doi/10.5555/1855768.1855793) of SSL notifications found to garner the highest interaction rates due to being perceived as a warning of potential danger.

![My banner design]({{site.baseurl}}/assets/images/whos-selling-my-info1/notification.png)

*The design of my notification: similar to our study design, but in attention-grabbing red and with a shorter message.*

## Developing the Extension

Before starting development, I learned the basics about browser extensions through the Mozilla Developer Network's [very helpful series of guides](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Your_first_WebExtension).  The first component of any browser extension is the `manifest.json` file, which provides overall information about the extension and links to its other files.  After setting basic information like a description and icon for the extension, the first thing the manifest does is point to a **background script**:
```json
  "background": {
    "scripts": [
      "background.js"
    ]
  }
```
This is a script that continually runs in the background for the extension and is used to perform any long-running tasks that persist between pages.  It runs in its own special DOM environment called the "background page," meaning it can't access elements from the websites a user visits.  For our purposes, that means that the background script can't search the page for an opt out link or inject a notification when one is found.  So for this extension, all the background script needs to do is listen for results from the script which will search the page, then change the extension's icon accordingly:
```javascript
// Add compatibility for Chromuim-based browsers
var browser = browser || chrome;

// Listen for search results
browser.runtime.onMessage.addListener(updateIcon);

// Update icon based on search result
function updateIcon(response){
    if(response.linkDetected == "yes"){
        browser.browserAction.setIcon({path: "icons/icon_active.png"});
    } else{
        browser.browserAction.setIcon({path: "icons/icon_inactive.png"});
    }
}
```

The other main component of `manifest.json` are links to **content scripts**.  These are files that will be loaded into pages whose URL matches a specific pattern:
```json
  "content_scripts": [
    {
      "matches": [
        "<all_urls>"
      ],
      "js": [
        "check_for_link.js",
        "click_scripts.js"
      ],
      "css": [
        "popup.css"
      ]
    }
  ]
```
In this case, we want our extension to run on every page the user visits, so we match `"<all_urls>"`.  Two scripts and one css files will be used on the page.  The first is the detection algorithm, `check_for_link.js`.  It implements a straightforward linear search of every page element for the target phrases:

```javascript
// Search page elements for CCPA opt-out link
var pageElements = document.getElementsByTagName('*');
var linkDetected = false;
var linkReference = null;
for (var i = 0; i < pageElements.length; i++) {

    // If opt-out link is found, display notification
    if (pageElements[i].innerHTML.toLowerCase().search('do not sell') != -1
        || pageElements[i].innerHTML.toLowerCase().search('don\'t sell') != -1) {
        linkReference = pageElements[i];
        linkDetected = true;
    }
}
```

If a link is detected, two things happen: first, a message is sent to the background script, which changes the extension icon's color to red.  Second, the following function is run to inject a notification overlaying the page:

```javascript
function displayPopup() {
    var popup = document.createElement('div');
    popup.setAttribute('id', 'CCPAPopup');

    var popupBody = document.createElement('div');
    popupBody.setAttribute('id', 'CCPABody');
    popupBody.innerHTML = '<b>This website sells your personal information.  Opt out below.</b></br>';
    popup.appendChild(popupBody);

    ... // Similar code here creates the more info link and close buttons

    var button = document.createElement('button');
    button.setAttribute('id', 'CCPAButton');
    button.innerHTML = "Don't Sell My Personal Information";
    popup.appendChild(button);

    // Add popup to document
    document.getElementsByTagName('BODY')[0].appendChild(popup);
}
```

Functionality then had to be added to the popup button.  This proved a bit tricker than expected.  Initially, I tried to extract the destination of the underlying site's opt-out link, then add it as a link to the button in my popup.  But I soon realized that not every website's opt-out link is actually a traditional "link" at all.  Some simply spawn a dialogue on the existing page when clicked and in fact have no destination to extract.  To work around this, I bound my button to a script that, when triggered, would simulate a click on the underlying page's opt out element:

```javascript
// Find and click CCPA opt-out link
    document.getElementById('CCPAButton').onclick = function () {
        var pageElements = document.getElementsByTagName('*');
        for (var i = 0; i < pageElements.length; i++) {
            // If opt-out link is found, click it.
            if (pageElements[i].innerHTML.toLowerCase().search('do not sell') != -1
                || pageElements[i].innerHTML.toLowerCase().search('don\'t sell') != -1) {
                pageElements[i].click();
            }
        }
    }
```

The final two pieces were straightfoward: first, a simple script removes the popup from the page when the user closes it.  Second, a CSS file provides styling for the popup.

## The Finished Product

![Our finished product working on a webpage]({{site.baseurl}}/assets/images/whos-selling-my-info1/testing.png)

*The finished extension working on a webpage.*

Put together, the extension works mostly as expected!  I manually tested it across the top 100 US websites and found that it successfully detects 91% of opt-out links with 0 false positives.  A couple of websites, such as [Adobe](https://www.adobe.com/) have links that fail to be detected for reasons that aren't immediately clear.  Furthermore, while false positives on top website homepages are rare, more niche content can inadvertently trigger the detection algorithm.  For example, this blog page with its extensive references to "do not sell" will be wrongly flagged as selling user data.

One limitation of the extension is that it only detects the 32% of websites that actually have a CCPA opt out link on their homepage.  A key finding of my research is that compliance with CCPA is still far from universal; about 1/3 of websites have failed to implement any response to CCPA's right to opt out of sale, and another significant minority have an opt out only in their privacy policy.  Future development could improve the extension by searching each site's privacy policy in addition to its homepage.  But ultimately, in the face of significant CCPA noncompliance, to fully know the extent of when users' information is being sold would require other methods of sale and tracking detection.

That being said, the extension successfully offers a non-trivial view into where a user's data is being sold as they browse the web.  It also empowers users to exercise their rights when they can, by bringing opt out links to a visible location on the page.  The finished extension can be installed from the Chrome or Firefox stores (links).  Thanks for reading, and feel free to contact me by [email](mailto:swow2015@mymail.pomona.edu) with questions or comments!  If you'd like to build on my work, the source code is freely available under an MIT license on [my GitHub](https://www.github.com/oapostrophe/whossellingmyinfo).