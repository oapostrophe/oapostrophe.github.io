---
layout: post
title:  "Privacy and the Dark Side of UI"
author: sean
categories: [ Privacy, User Interface, Dark Patterns, CCPA ]
image: assets/images/ccpa1/tracking-image.jpg
featured: false
hidden: false
description: "Blog post discussing how UI dark patterns subvert the effect of the California Consumer Privacy Act"
comments: false
---

*How User Interface Dark Patterns stop consumers from opting out of personal information sales.*

*Special thanks to my collaborators [Ryan Nurwono](https://www.linkedin.com/in/ryan-nurwono/) and Professor [Eleanor Birrell](https://cs.pomona.edu/~ebirrell/index.html).*

Over the past decade, digital tracking and the online sale of personal information has exploded.  When visiting a website or opening a mobile app, you can now expect almost everything you do to be [tracked](https://crackedlabs.org/en/corporate-surveillance): not just by the company you're visiting, but by dozens of other companies [bidding for ads on the page](https://www.eff.org/wp/behind-the-one-way-mirror#Part3), [social media websites](https://www.wired.com/story/ways-facebook-tracks-you-limit-it/), the [search engine that referred you](https://spreadprivacy.com/what-does-google-know-about-me/), and the website's [analytics service providers](https://developers.google.com/analytics/resources/concepts/gaConceptsTrackingOverview).  Almost [every page you visit](https://whotracks.me/companies/reach-chart.html), what you do there, and information like the location and time from which you did so are now surveilled by third parties.  In essence, the websites you're visiting sell information about what you do there to companies called ["data brokers"](https://www.eff.org/wp/behind-the-one-way-mirror#Data-brokers), who collect it all into one large, central profile.

These data brokers have amassed extensive profiles on billions of people across the globe, often containing thousands of pieces of information including race, gender identity, sexual orientation, political and religious beliefs.  Data brokers know where you live, work, and travel.  They know your shopping and [dating preferences](https://www.engadget.com/2020-01-14-study-finds-grindr-okcupid-tinder-spreading-sensitive-data.html).  They track your medical and psychiatric history.  They also use AI to analyze the enormous amount of information they've stored on you and draw inferences about topics like [your risk to medical insurers](https://www.wsj.com/articles/SB10001424052748704648604575620750998072986), what political messaging you'll respond to, and how likely you are to commit a crime.

![Examples of information included in Data Broker Profiles]({{site.baseurl}}/assets/images/ccpa1/data-broker-profiles.jpg)

*Examples of information included in Data Broker Profiles.*

What's more, in the world of smart appliances, data harvesting goes beyond just your internet browsing.  Carrying a smartphone at all times [enables our location history to be silently tracked](https://myshadow.org/location-tracking) and sold by apps we've installed, Wi-Fi networks we pass, and [even](https://www.eff.org/press/releases/eff-sues-att-data-aggregators-giving-bounty-hunters-and-other-third-parties-access) our [phone network providers](https://www.vice.com/en/article/nekm87/verizon-stop-selling-phone-location-data-wyden-securus-locationsmart).  Internet-connected medical devices like CPAP machines [secretly sell](https://www.propublica.org/article/you-snooze-you-lose-insurers-make-the-old-adage-literally-true) usage data to insurance companies.  Every time you swipe your credit card, payment processing companies, [not subject to the same strict data protection regulations as banks](https://www.ftc.gov/system/files/documents/public_comments/2016/11/00035-129640.pdf), can log and sell the transaction data.  "Smart" appliances like TVs, thermostats, laundry machines, even electric toothbrushes all [have the potential to track and sell your activity](https://www.theguardian.com/commentisfree/2021/apr/05/tech-police-surveillance-smart-home-devices).


![If only all tracking was this wholesome]({{site.baseurl}}/assets/images/ccpa1/tracking-meme.jpg)

What is such information used for, other than uncannily targeted ads following you around the internet?  Here are just a few things that we know of:
- The US military, who we know [uses phone metadata for targeting drone strikes](https://www.vice.com/en/article/3da8n9/the-problem-with-using-metadata-to-justify-drone-strikes), buys location data in bulk--including that [harvested from a popular Muslim prayer app](https://www.vice.com/en/article/jgqm5x/us-military-location-data-xmode-locate-x).
- Radical anti-abortion groups used location data to [target anti-choice ads](https://rewirenewsgroup.com/article/2016/05/25/anti-choice-groups-deploy-smartphone-surveillance-target-abortion-minded-women-clinic-visits/) at pregnant people in abortion clinic waiting rooms.
- Major credit agencies use a wide range of harvested behavioral data to assign people profiles with names like ["credit hungry card switcher"](https://www.experian.com/assets/marketing-services/product-sheets/audience-lookbook.pdf), which influence their credit score, opportunities for loans, and ability to obtain housing.  
- Local law enforcement can obtain "geofencing" warrrants that allow them to blindly request the data of anyone whose device was near the scene of a crime, which has led to innocent people wrongfully [becoming crime suspects](https://www.nbcnews.com/news/us-news/google-tracked-his-bike-ride-past-burglarized-home-made-him-n1151761) and in at least one case even [jailed for a murder they didn't commit](https://www.phoenixnewtimes.com/news/google-geofence-location-data-avondale-wrongful-arrest-molina-gaeta-11426374).  
- [Federal law enforcement agencies](https://www.wsj.com/articles/federal-agencies-use-cellphone-location-data-for-immigration-enforcement-11581078600), who among other things conduct surveillance campaigns on US citizens [based on their race](https://www.thenation.com/article/archive/surveillance-muslim-technology/) or [participation in non-violent protests](https://www.aclu.org/issues/racial-justice/protectblackdissent-campaign-end-surveillance-black-activists), freely [buy information about citizens](https://www.cnet.com/news/without-warrants-intelligence-agency-buys-location-data-on-us-residents/) without ever obtaining a search warrant.
- Civilian [bounty hunters](https://www.vice.com/en/article/nepxbz/i-gave-a-bounty-hunter-300-dollars-located-phone-microbilt-zumigo-tmobile) and [bail bond companies](https://www.vice.com/en/article/9k873e/captira-phone-tracking-verizon-tmobile-sprint-securus-locationsmart-bounty-hunters) buy location data to track targets.  
- Psychological profiles harvested from social media are used to [manipulate elections](https://www.accessnow.org/your-data-used-against-you-reports-of-manipulation-on-whatsapp-ahead-of-brazils-election/) and were used in [Trump's 2016 campaign](https://www.cnet.com/news/facebook-cambridge-analytica-data-mining-and-trump-what-you-need-to-know/) for hyper-targeted political messaging.  
- Personal data can silently change the opportunities that are shown to you as you browse the web; for instance, [job openings you see](https://www.wired.com/story/facebooks-ad-system-discrimination/) become different depending on your race and gender.  

Ultimately, no one knows the full extent of who is using such information, how, and why, but what we do know is more than cause for concern.

You might wonder: when you visit a website or download an app onto your phone, how can they know who you are?  After all, most people routinely visit pages to whom they've never given their name.  But in today's world, any website you visit can know who you are before the page finishes loading.  Several pieces of information routinely transmitted by your browser are enough to create a ["fingerprint" that uniquely identifies you](https://coveryourtracks.eff.org/static/browser-uniqueness.pdf): your IP address, operating system, browser version, etc.  Sites also frequently use [tracking cookies](https://privacy.net/stop-cookies-tracking/) that store a unique identifier to remember who you are across the web.  Pages receiving your browser fingerprint or tracking cookie id can bring them to data brokers and third-party advertisers, who can then link them to a larger profile of information collected from your visits to other sites, including ones where you've given personally identifiable information such as your full name and date of birth.  In effect, such personally identifiable information follows you around the internet, linking all your browsing together into one profile.  The result is the kind of pervasive surveillance that's previously only been imagined in dystopian science fiction.

![Data aggregation]({{site.baseurl}}/assets/images/ccpa1/data-aggregation.png)

*The process of data aggregation and identification.*

## California Steps in

In July 2020, a [California law](https://www.oag.ca.gov/privacy/ccpa) aiming to address these issues took effect.  Among other things, the California Consumer Privacy Act (CCPA) requires that companies give California users the right to opt out from the sale of their personal information to third parties.  While previous US privacy laws have considered "personal information" to be direct identifiers like your name and date of birth, the CCPA critically uses a [broader definition](https://www.oag.ca.gov/privacy/ccpa).  It defines personal information to include any information that "identifies, relates to, or **could reasonably be linked with you or your household.**"  This means that the exchanges made during targeted advertising and third-party tracking, where non-identifying information is sold attached a cookie ID or browser fingerprint identifiable to the buyer, are now considered personal information sales under the law.  CCPA requires that all websites making such sales display a "clear and conspicuous" opt out link titled "Do Not Sell My Personal Information".

When the law became enforceable on July 1, 2020, I joined Pomona College's Privacy and Security Lab to study: how is this new requirement actually being implemented by companies?  History has shown that when a [similar law](https://gdpr-info.eu/) was passed in the EU, [a vast majority of companies](https://dl.acm.org/doi/pdf/10.1145/3319535.3354212) failed to comply and subverted the law's impact through the user interface (UI) of their privacy choices.  For instance, more than 95% of companies designed EU-mandated cookie consent banners where the only option was to accept or leave the page, in blatant violation the law.  Of those that provided a decline option, many used UI "Dark Patterns" to trick users into accepting.  We wanted to know: would US companies respond similarly to CCPA, or would they comply with the law and create effective opt outs?

## Failure to Comply

Under the guidance of Professor Eleanor Birrell, I led an investigation into how companies responded to the new requirements. I first analysed the top 500 California websites as [repoted by Amazon Alexa](https://www.alexa.com/topsites/countries/US).  Disappointingly, I found that just 42.6% of websites had any CCPA opt out on their site.  32.6% had no reference to CCPA's sale opt out, which given the nearly ubiquitous presence of third-party tracking, likely means they sell information and are simply ignoring the law.  Another 23.2% claim that they don't sell personal information under CCPA's definition; however, such statements often included claims that providing their users' data to third-party advertising services don't constitute a "sale" of information, despite this being the exact activity targeted by CCPA.  On the whole, given how widespread we know personal information sale to be, the ability to opt out on just 42.6% of sites means that CCPA is a long ways from universal compliance.

![Denial of sale]({{site.baseurl}}/assets/images/ccpa1/third-party-tracking-denial.png)

*Many sites claiming they don't need a CCPA opt out also admit, in convoluted terms, to selling your information.*

What's worse, among the 42.6% of sites that did implement some sort of sale opt out, numerous design issues compromise users' ability to exercise their rights.  While CCPA requires opt out links to be "clear and conspicuous", 73% of these sites instead required users to scroll (often a great distance) to the bottom of their page, where the link was buried in small font among other rarely-visited topics like "Legal information" and "Privacy Policy".  Another 16% explicitly violated CCPA's requirements by including no link at all, instead hiding instructions for opt out in their privacy policy.  Just 8% of pages displayed their link in an immediately visible banner, showing that a clear and conspicuous opt out is possible—most companies simply choose not to implement one.

![A typical CCPA Link]({{site.baseurl}}/assets/images/ccpa1/ccpa-link.png)

*A typical CCPA link, far from "Clear and Conspicuous".  Note how far down the page is scrolled.*

If users manage to find these links at all, the process only gets more difficult from there.  Only 42% of websites' links led to any sort of direct, in-website opt out mechanism such as a button, checkbox, toggle, etc.  50% of pages instead required users to fill out a form or contact the company, then wait to hear back about their request. [Another study](https://advocacy.consumerreports.org/wp-content/uploads/2021/05/CR_CCPA-Are-Consumers-Digital-Rights-Protected_092020_vf2.pdf) of these contacts found that in response, companies were extremely slow, difficult to deal with, and requested excessive amounts of personal information before allowing users to opt out.  25% of opt outs directed users to third-party targeted advertising opt out sites, which don't actually stop the sale of personal information, since they allow [half of participating advertisers](https://ieeexplore.ieee.org/document/8844599) to continue collecting information about users after being placed.  38% of opt outs required users to complete more than one process to opt out from different types of information sale; these sites' instructions were frequently convoluted, missing key information, and sometimes even self-contradictory.  For instance, one site instructed users to visit **16 different third-party websites** and file requests with them separately.

![Multiple third parties]({{site.baseurl}}/assets/images/ccpa1/multiple-third-parties.png)

*Many opt outs were effectively unusable.  Imagine searching every one of these services' privacy policies and trying to find how to opt out.*

Even among the opt outs that implemented a direct on-site mechanism, UI barriers to opt out were common.  We found design Dark Patterns present in 84% of these opt outs.  These are patterns that aim to nudge or deceive the user into allowing the sale of their data: for example, highlighting the "accept" button while making "decline" physically smaller, pre-checking the option to accept data sale by default, or pop-ups asking the user "Are you sure?" before they can opt out.  Such patterns have a long history of use [throughout the web](https://www.darkpatterns.org/types-of-dark-pattern) in a variety of contexts, but are [especially frequent](https://fil.forbrukerradet.no/wp-content/uploads/2018/06/2018-06-27-deceived-by-design-final.pdf) when companies have to design privacy choices.

![Example of dark patterns in a banner: the OK button is highlighted, and "Do Not Sell" option is to the side in small text]({{site.baseurl}}/assets/images/ccpa1/nudging.png)

*Dark Patterns at work: the "OK" button is highlighted, while "Do Not Sell" is in small text on the side.*

## How do these designs affect user behavior?

These findings seem bad.  But to check that hypothesis, we created an experimental website where we could put different CCPA designs to the test.  Our site, "All Sides News", displayed top news stories filtered by political leaning.  This created an everyday browsing context where even a casual visitor might be vulnerable to having sensitive personal information about them sold.  For example, the sections and articles that a visitor clicks could reveal their political alignment and interests.

![Our website]({{site.baseurl}}/assets/images/ccpa1/all-sides-news.png)

*Our website, which aggregated news stories from various sources and filtered them by political leaning.*

We had two groups of California-based users visit our website: the first were recruited through Amazon Mechanical Turk.  These users were paid to visit our website and browse as they normally would under the pretense of beta testing a news website.  They then returned to Amazon and completed a brief follow-up survey.  A second group of users was recruited through Google Ads; for these users, no instructions or follow-up survey were offered and we simply observed how they interacted with the website.

![Our google ad]({{site.baseurl}}/assets/images/ccpa1/google-ad.png)

*The Google Ad shown for our website.*

When entering the page, users were randomly assigned to different designs of CCPA opt out.  We did two sets of experiments: the first one compared different banner locations to a link at the bottom of the page.  The second experiment measured the effect of various Dark Patterns (such as highlighting the "accept" button) and inconvenience factors (such as having to fill out a form).  After showing a CCPA notice, we logged each user's activity on the page under an anonymized identifier (contrary to what our website told users, no personally identifiable information was actually collected during the study).

![Our ccpa banner]({{site.baseurl}}/assets/images/ccpa1/banner.png)

*One of the mock CCPA banners displayed on our site (location and design varied by study condition).*

The results show that almost all of the design elements we saw companies implement significantly reduced how many users opted out of having their personal information sold.  Unsurprisingly, when "Do Not Sell My Personal Information" was placed as a small link at the bottom of the website instead of shown in a banner, users were significantly less likely to interact with it (p < 0.001).  While 14% of Google Ads users used our opt out when it was displayed in a banner, **just 1% of users from Google Ads clicked our link at the bottom of the page to opt out.**  Mechanical Turk opt out similarly decreased from 19.3% to 8.6%, and users shown a banner were 16.6% more likely to be aware they had an option to opt out from information sale on the page.  Dark Patterns and changing the opt out to an indirect mechanism also significantly decreased how many users opted out.  The only exception was that highlighting the "accept" button made users no less likely to decline information sales.

## The Road Ahead

Our results show that despite the beginning of CCPA's enforcement period, California consumers don't yet have the right to universally opt out from the sale of personal information.  Less than half of sites even have an opt out, those that do are hard to find and difficult to use, and many don't even stop your information from being sold.  These factors could all potentially be improved through enforcement and stronger guidelines about usable opt out design.  But there's also a bigger issue: no matter how visible and easy to use they are individually, opt outs that require users to separately file them with every company will remain ineffective as a whole.

Even in our most visible, easy-to-use study condition, most users who said they were uncomfortable with our site selling their information didn't use our opt out.  This tracks with what prior research has found: in general, privacy choices aren't people's main objective when coming to a website, so they don't frequently interact with them even in the absence of UI Dark Patterns.  As such, offering users an individual choice to opt out doesn't work to create the privacy practices they would actually want to see followed.  Furthermore, even for a highly motivated user who does engage with opt outs, switching off information sale altogether would be an impractical amount of work.  In addition to needing to opt out on the hundreds of websites they've visited in their lifetime, such users would also have to file separate requests with [over 200 data brokers registered in California](https://www.oag.ca.gov/data-brokers).  Thus, even in a hypothetical future where all the problems we've identified are fixed, CCPA opt outs will be far from a solution to the privacy issues of our time.

![do-not-track]({{site.baseurl}}/assets/images/ccpa1/do-not-track.png)

*Browser signals could be a more user-friendly way to implement privacy opt outs.*

One alternative model could be the "Do Not Track" browser signal also introduced by CCPA, but currently lacking clear guidelines for how it should be followed by companies.  This would let users change a browser option to opt out from tracking everywhere they go in a single step.  Another privacy framework is the affirmative consent model of the EU's GDPR, which requires users to opt-in to tracking instead of opting out; however, as discussed above, this model has been widely violated by companies in practice.  An individual choice model for privacy could also be eschewed entirely in favor of collective regulations on data sale and third-party tracking.  Companies could also enact voluntary change to privacy-friendly methods of advertising and monetization, which don't require ubiquitous tracking and profiling of populations.  Whatever the road forward, it's clear that CCPA is not the end of the privacy discussion; it's only the beginning.

*For more, check out our full [tech report](https://arxiv.org/abs/2009.07884), and stay tuned for the publication of this study along with follow-up work on how our findings have evolved since Summer 2020.  If you have questions or comments, I'd love to hear from you!  Just send me an [email](mailto:swow2015@mymail.pomona.edu).*