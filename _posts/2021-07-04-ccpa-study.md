---
layout: post
title:  "How do companies comply with ccpa?"
author: sean
categories: [ Privacy, User Interface, Dark Patterns, CCPA ]
image: assets/images/heartnet1/banner_image.jpg
featured: false
hidden: true
description: "Blog post discussing how UI dark patterns subvert the effect of the California Consumer Privacy Act"
comments: false
---

*How UI Dark Patterns stop consumers from opting out of personal information sales.*

*Special thanks to my collaborators [Ryan Nurwono](https://www.linkedin.com/in/ryan-nurwono/) and Professor [Eleanor Birrell](https://cs.pomona.edu/~ebirrell/index.html).*

Over the past two decades, digital tracking and the online sale of personal information has exploded.  When visiting a website or opening a mobile app, you can now expect almost everything you do to be [tracked](https://crackedlabs.org/en/corporate-surveillance): not just by the company you're visiting, but by dozens of other companies [bidding for ads on the page](https://www.eff.org/wp/behind-the-one-way-mirror#Part3), [social media websites](https://www.wired.com/story/ways-facebook-tracks-you-limit-it/), the [search engine that referred you](https://spreadprivacy.com/what-does-google-know-about-me/), and the website's [analytics service providers](https://developers.google.com/analytics/resources/concepts/gaConceptsTrackingOverview).  Almost [every page you visit](https://whotracks.me/companies/reach-chart.html), what you do there, and information like the location and time from which you did so are now tracked by third parties.  In essence, the websites you're visiting sell information about what you do there, which ends up being re-sold until it's eventually collected by companies called ["data brokers"](https://www.eff.org/wp/behind-the-one-way-mirror#Data-brokers).

These data brokers have amassed extensive profiles on billions of people across the globe, often containing thousands of pieces of information including sensitive attributes like race, gender identity, sexual orientation, political and religious beliefs.  Data brokers know where you live, work, and travel.  They know your shopping and [dating preferences](https://www.engadget.com/2020-01-14-study-finds-grindr-okcupid-tinder-spreading-sensitive-data.html).  They track your medical and psychiatric history.  They also use AI to analyze the enormous amount of information they've stored on you and draw inferences about topics like [your health and risk to medical insurers](https://www.wsj.com/articles/SB10001424052748704648604575620750998072986), what political messaging you'll respond to, and how likely you are to commit a crime.

![Examples of information included in Data Broker Profiles]({{site.baseurl}}/assets/images/ccpa1/data-broker-profiles.jpg)

*Examples of information included in Data Broker Profiles.*

What's more, in the world of smart appliances, data harvesting goes beyond just your internet browsing.  Carrying a smartphone at all times [enables our location history to be silently tracked](https://myshadow.org/location-tracking) and sold by apps we've installed (including when we're not using them), wifi networks we pass, and [even](https://www.eff.org/press/releases/eff-sues-att-data-aggregators-giving-bounty-hunters-and-other-third-parties-access) our [phone network providers](https://www.vice.com/en/article/nekm87/verizon-stop-selling-phone-location-data-wyden-securus-locationsmart).  Internet-connected medical devices like CPAP machines [secretly sell](https://www.propublica.org/article/you-snooze-you-lose-insurers-make-the-old-adage-literally-true) usage data to insurance companies.  Every time you swipe your credit card, payment processing companies, [not subject to the same strict data protection regulations as banks](https://www.ftc.gov/system/files/documents/public_comments/2016/11/00035-129640.pdf), can log and sell the transaction data.  "Smart" appliances like TVs, thermostats, laundry machines, even electric toothbrushes all [have the potential to track and sell your activity](https://www.theguardian.com/commentisfree/2021/apr/05/tech-police-surveillance-smart-home-devices).


![If only all tracking was this wholesome]({{site.baseurl}}/assets/images/ccpa1/tracking-meme.jpg)

*We can only guess the full extent of who's buying this information and for what purposes.*

What is such information used for, other than uncannily targeted ads following you around the internet?  Here are just a few things that we know of:
- The US military, who we know [uses phone metadata for targeting drone strikes](https://www.vice.com/en/article/3da8n9/the-problem-with-using-metadata-to-justify-drone-strikes), buys location data in bulk--including that [harvested from a popular Muslim prayer app](https://www.vice.com/en/article/jgqm5x/us-military-location-data-xmode-locate-x).
- [Federal law enforcement agencies](https://www.wsj.com/articles/federal-agencies-use-cellphone-location-data-for-immigration-enforcement-11581078600), who among other things conduct surveillance campaigns on innocent US citizens [based on their race](https://www.thenation.com/article/archive/surveillance-muslim-technology/) or [participation in non-violent protests](https://www.aclu.org/issues/racial-justice/protectblackdissent-campaign-end-surveillance-black-activists), freely [buy information about citizens](https://www.cnet.com/news/without-warrants-intelligence-agency-buys-location-data-on-us-residents/) without ever obtaining a search warrant.
- Local law enforcement can obtain "geofencing" warrrants that allow them to blindly request the data of anyone whose device was near the scene of a crime, which has led to innocent people wrongfully [becoming crime suspects](https://www.nbcnews.com/news/us-news/google-tracked-his-bike-ride-past-burglarized-home-made-him-n1151761) and in at least one case even [jailed for a murder they didn't commit](https://www.phoenixnewtimes.com/news/google-geofence-location-data-avondale-wrongful-arrest-molina-gaeta-11426374).  
- Civilian [bounty hunters](https://www.vice.com/en/article/nepxbz/i-gave-a-bounty-hunter-300-dollars-located-phone-microbilt-zumigo-tmobile) and [bail bond companies](https://www.vice.com/en/article/9k873e/captira-phone-tracking-verizon-tmobile-sprint-securus-locationsmart-bounty-hunters) buy location data to track targets.  
- Radical anti-abortion groups used location data to [target anti-choice ads](https://rewirenewsgroup.com/article/2016/05/25/anti-choice-groups-deploy-smartphone-surveillance-target-abortion-minded-women-clinic-visits/) at pregnant people in abortion clinic waiting rooms.  
- Psychological profiles harvested from social media are used to [manipulate elections](https://www.accessnow.org/your-data-used-against-you-reports-of-manipulation-on-whatsapp-ahead-of-brazils-election/) and were used in [Trump's 2016 campaign](https://www.cnet.com/news/facebook-cambridge-analytica-data-mining-and-trump-what-you-need-to-know/) for hyper-targeted political messaging.  
- Major credit agencies use a wide range of harvested behavioral data to assign people profiles with names like ["credit hungry card switcher"](https://www.experian.com/assets/marketing-services/product-sheets/audience-lookbook.pdf), which influence their credit score and opportunities for loans and housing.  
- Personal data can silently change the opportunities that are shown to you as you browse the web; for instance, [job openings you see](https://www.wired.com/story/facebooks-ad-system-discrimination/) become different depending on your race and gender.  

Ultimately, no one knows the full extent of who is using such information, how, and why, but what we do know is more than cause for concern.

You might wonder: when you visit a website or download an app onto your phone, how can they know who you are?  After all, most people use websites and apps where they never give their name.  But in today's world, a website doesn't need your name to know who you are.  Several pieces of information routinely transmitted by your browser to websites are enough to create a ["fingerprint" that uniquely identifies you](https://coveryourtracks.eff.org/static/browser-uniqueness.pdf): your IP address, operating system, browser version, etc.  Sites also frequently use [tracking cookies](https://privacy.net/stop-cookies-tracking/) that store a unique identifier to remember who you are across the web.  Pages receiving your browser fingerprint or tracking cookie id can bring them to third-party trackers and data brokers, who can then link them to a larger profile of information collected from your visits to other sites, including ones where you've given personally identifiable information such as your full name and date of birth.  In effect, such personally identifiable information follows you around the internet, linking all your browsing together into one profile.  The result is the kind of pervasive surveillance that's previously only been imagined in dystopian science fiction.

![Data aggregation]({{site.baseurl}}/assets/images/ccpa1/data-aggregation.png)

*A diagram illustrating the process of data aggregation and identification.*

## California Steps in

In July 2020, a [California law](https://www.oag.ca.gov/privacy/ccpa) aiming to address these issues took effect.  Among other things, the California Consumer Privacy Act (CCPA) requires that companies give California users the right to opt out from the sale of their personal information to third parties.  While previous US privacy laws have considered "personal information" to be direct identifiers like your name and date of birth, the CCPA critically uses a [broader definition](https://www.oag.ca.gov/privacy/ccpa).  It defines personal information to include any information that "identifies, relates to, or **could reasonably be linked with you or your household.**"  This means that the exchanges made during targeted advertising and third-party tracking, where non-identifying information is sold attached a cookie ID or browser fingerprint identifiable to the buyer, are now considered personal information sales under the law.  CCPA requires that all websites making such sales display a "clear and conspicuous" opt-out link titled "Do Not Sell My Personal Information".

When the law became enforceable on July 1, 2020, I joined Pomona College's Privacy and Security Lab to study: how is this new requirement actually being implemented by companies?  History has shown that when a [similar law](https://gdpr-info.eu/) was passed in the EU, [a vast majority of companies](https://dl.acm.org/doi/pdf/10.1145/3319535.3354212) failed to comply and subverted the law's impact through the user interface (UI) of their privacy choices.  For instance, upwards of 95% of companies designed EU-mandated cookie consent banners where the only option was to accept or leave the page, in blatant violation the law.  Of those that provided a decline option, many used UI "Dark Patterns" to try tricking users into accepting.  We wanted to know: would US companies respond similarly to CCPA, or would they comply with the law and create effective opt-outs?

## Failure to Comply

Under the guidance of Professor Eleanor Birrell, I led an investigation into how many companies are following the new requirements, the UI designs they're using to do so, and how these designs affect users' ability to exercise their CCPA rights.  I first analysed the top 500 California websites as [repoted by Amazon Alexa](https://www.alexa.com/topsites/countries/US).  Disappointingly, I found that just 42.6% of websites had any CCPA opt-out on their site.  32.6% had no reference to CCPA's sale opt-out anywhere on their site, which given the ubiquitous presence of third-party tracking, likely means they sell information and are simply ignoring the law.  Another 23.2% claim that they don't sell personal information under CCPA's definition; however, such statements often included claims that providing their users' data to third-party tracking and targeted advertising services don't constitute a "sale" of information, despite this being the exact activity targeted by CCPA.  On the whole, given how ubiquitous we know personal information sale to be, the ability to opt out on just 42.6% of sites means that CCPA is a long ways from universal compliance.

![Websites' compliance with CCPA]({{site.baseurl}}/assets/images/ccpa1/compliance-pie-chart.png)

*A chart of website compliance with CCPA: just 42.6% offer a way to opt out.*

![Denial of sale]({{site.baseurl}}/assets/images/ccpa1/third-party-tracking-denial.png)

*As seen here, many of the 23.2% of sites claiming they don't sell information under CCPA admit to exactly the activities targeted by the law: selling your information to third party trackers and advertisers.*

What's worse, among the 42.6% of sites that did implement some sort of sale opt-out, there were numerous design issues that usually compromised users' ability to actually exercise their rights.  While CCPA requires such links to be "clear and conspicuous", 73% of these sites instead required users to scroll (often a great distance) to the bottom of their page, where the link was buried in small font within a list of other rarely-visited topics like "Legal information" and "Privacy Policy".  Another 16% explicitly violated CCPA's requirements by including no link at all, instead placing instructions for opt-out in their privacy policy.  Just 8% of pages displayed their link in an immediately visible banner, showing that a clear and conspicuous opt-out is possible—most companies simply choose not to implement one.

![A typical CCPA Link]({{site.baseurl}}/assets/images/ccpa1/ccpa-link.png)

*A typical CCPA link, far from "Clear and Conspicuous".*

If users manage to find these links at all, the process only gets more difficult from there.  Only 42% of websites' links led to any sort of direct, in-website opt-out mechanism such as a button, checkbox, toggle, etc.  50% of pages instead required users to fill out a form or contact the company, then wait to hear back about their request. [Another study](https://advocacy.consumerreports.org/wp-content/uploads/2021/05/CR_CCPA-Are-Consumers-Digital-Rights-Protected_092020_vf2.pdf) of these contacts found that in response, companies were frequently slow to respond, difficult to deal with, and requested excessive amounts of personal information before allowing users to opt out.  25% of opt outs directed users to third-party targeted advertising opt out sites, which don't actually stop the sale of personal information, since they allow [half of participating advertisers](https://ieeexplore.ieee.org/document/8844599) to continue collecting information about users after being placed.  38% of opt outs actually required users to complete more than one opt out process to opt out from different types of information sale; these sites' instructions were frequently convoluted, missing key information, and sometimes even self-contradictory.  For example, one such page first instructed users to save an opt-out cookie, then in another part of the instructions told the user to disable cookies entirely. Another site instructed users to visit 16 different third-party websites and file opt-out requests with them separately.  

![Multiple third parties]({{site.baseurl}}/assets/images/ccpa1/multiple-third-parties.png)

*Many opt outs were effectively unusable.  Imagine trying to figure out how to opt out from all these services' privacy policies.*

Even among the opt-outs that implemented a direct on-site opt out mechanism, UI barriers to opt-out were common.  We found design "Dark Patterns" present in 84% of these opt-outs.  These are patterns that aim to "nudge" or deceive the user into allowing the sale of their data: for example, highlighting the "accept" button while making "decline" physically smaller, pre-checking the option to accept data sale by default, or pop-ups asking the user "Are you sure?" before they can opt out.  Such patterns have a long history of use [throughout the web](https://www.darkpatterns.org/types-of-dark-pattern) in a variety of contexts, but are [especially frequent](https://fil.forbrukerradet.no/wp-content/uploads/2018/06/2018-06-27-deceived-by-design-final.pdf) when companies have to design privacy choices.

![Example of dark patterns in a banner: the OK button is highlighted, and "Do Not Sell" option is to the side in small text]({{site.baseurl}}/assets/images/ccpa1/nudging.png)

*Example of dark patterns in a CCPA banner: the OK button is highlighted, while the "Do Not Sell" option is to the side in small text.*

## How do these designs affect user behavior?

These findings seem bad.  But to confirm that hypothesis, we created an experimental website where we could put different CCPA designs to the test.  Our site, "All Sides News", displayed top news stories filtered by political leaning.  This created an everyday browsing context where even a casual visitor might be vulnerable to having sensitive personal information about them sold.  For example, the sections and articles that a visitor clicks could reveal their political alignment and interests.

![Our website]({{site.baseurl}}/assets/images/ccpa1/all-sides-news.png)

*Our website, which aggregated news stories from various sources and filtered them by political leaning.*

We had two groups of California-based users visit our website: the first were recruited through Amazon Mechanical Turk.  These users were paid to visit our website and browse as they normally would under the pretense of beta testing a news website.  They then returned to Amazon and completed a brief follow-up survey.  A second group of users was recruited through Google Ads; for these users, no instructions or follow-up survey were offered and we simply observed how they interacted with the website.

![Our google ad]({{site.baseurl}}/assets/images/ccpa1/google-ad.png)

*The Google Ad shown for our website.*

When entering the page, users were randomly assigned to different designs of CCPA opt-out based on their IP address.  We did two sets of experiments: the first one compared different banner locations to a link at the bottom of the page.  The second experiment measured the effect of various Dark Patterns (such as highlighting the "accept" button) and inconvenience factors (such as having to fill out a form or un-check multiple boxes).  After showing a CCPA notice, we logged each user's activity on the page under an anonymized identifier (contrary to what our website told users, no personally identifiable information was actually collected during the study).

![Our ccpa banner]({{site.baseurl}}/assets/images/ccpa1/banner.png)

*The mock CCPA banner displayed on our site (we tested it displayed in various conditions across the page).*

The results show that almost all of the design elements we saw companies implement significantly reduced how many users opted out of having their personal information sold.  Unsurprisingly, when "Do Not Sell My Personal Information" was placed as a small link at the bottom of the website instead of shown in a banner, users were significantly less likely to interact with it (p < 0.001).  While 14% of Google Ads users used our opt out when it was displayed in a banner, **just 1% of users from Google Ads clicked our link at the bottom of the page to opt out.**  Mechanical Turk opt-out similarly decreased from 19.3% to 8.6%, and users shown a banner were 16.6% more likely to be aware they had an option to opt out from information sale on the page.  Dark Patterns and changing the opt-out to an indirect mechanism such as a fillable form also significantly decreased how many users opted out.  The only exception was that highlighting the "accept" button made users no less likely to decline information sales.








Finally, our results suggest that privacy regulations that dependon individual opt-out may be inherently flawed. Across all condi-tions in our user studies, most participants who expressed discom-fort with our example site selling their data did not actually utilizethe opt-out mechanism on our site. This reinforces prior findingsthat opt-out mechanisms discourage engagement, a problem thatis exacerbated in the online ecosystem due to the large number ofindividual sites and data brokers that collect personal informationabout users (for example, there are over 200 data brokers registeredin California [28], in addition to the potentially hundreds or thou-sands of websites with whom a user has direct relationships). Tocompletely opt out from the sale of their information, consumerswould have to separately file opt-out requests with every one ofthese companies. Given the current state of compliance with CCPAobserved in our studies, entirely preventing the sale of one’s dataremains infeasible. As such, efforts that go beyond the implemen-tation of CCPA’s sale opt-out, such as the adoption of Do Not Sellbrowser signals or future legislation to limit data sale, will be criticalfor enhancing user privacy at scale




Link to tech report:
https://arxiv.org/abs/2009.07884




<h2><a id="Citations">Citations</a></h2>

1. [Heart disease and stroke statistics—2021 update](https://www.heart.org/-/media/phd-files-2/science-news/2/2021-heart-and-stroke-stat-update/2021_heart_disease_and_stroke_statistics_update_fact_sheet_at_a_glance.pdf?la=en): a report from the American Heart Association
2. Bång, Angela, Lars Grip, Johan Herlitz, Stefan Kihlgren, Thomas Karlsson, Kenneth Caidahl, and Marianne Hartford. ["Lower mortality after prehospital recognition and treatment followed by fast tracking to coronary care compared with admittance via emergency department in patients with ST-elevation myocardial infarction."](https://www.sciencedirect.com/science/article/pii/S0167527307016579?casa_token=QwM9I3I5klIAAAAA:1BTMwOBPmN4yl27K4MK_dxenVVpPWVXrzWEmp2Sid99Vjj-018TLvvhR7CRVz5MGYgCmvs4a_A) International journal of cardiology 129, no. 3 (2008): 325-332.
3. Turner, A., Dunne, R. and Wise, K., 2017. National Institute For Health Care Reform. [online] Nihcr.org. Available at: [<https://nihcr.org/wp-content/uploads/2017/06/NIHCR_Altarum_Detroit_EMS_Brief_5-30-17.pdf>](https://nihcr.org/wp-content/uploads/2017/06/NIHCR_Altarum_Detroit_EMS_Brief_5-30-17.pdf) [Accessed 8 May 2021].
4. Mary Colleen Bhalla, Francis Mencl, Mikki Amber Gist, Scott Wilber & Jon Zalewski (2013) [Prehospital Electrocardiographic Computer Identification of ST-segment Elevation Myocardial Infarction](https://www.tandfonline.com/doi/abs/10.3109/10903127.2012.722176), Prehospital Emergency Care, 17:2, 211-216, DOI: 10.3109/10903127.2012.722176
5. Hartman, Stephanie M., Andrew J. Barros, and William J. Brady. ["The use of a 4-step algorithm in the electrocardiographic diagnosis of ST-segment elevation myocardial infarction by novice interpreters."](https://emupdates.com/wp-content/uploads/2008/07/Hartman-4-Steps-to-STEMI-Diagnosis-AmJEM-2012.pdf) The American journal of emergency medicine 30, no. 7 (2012): 1282-1295.
6. Mehta, S., F. Fernandez, C. Villagran, A. Frauenfelder, C. Matheus, D. Vieira, M. A. Torres et al. ["P1466 Can physicians trust a machine learning algorithm to diagnose ST elevation myocardial infarction?."](https://academic.oup.com/eurheartj/article-abstract/40/Supplement_1/ehz748.0231/5598215) European Heart Journal 40, no. Supplement_1 (2019): ehz748-0231.
7. Liu, Wenhan, Mengxin Zhang, Yidan Zhang, Yuan Liao, Qijun Huang, Sheng Chang, Hao Wang, and Jin He. ["Real-time multilead convolutional neural network for myocardial infarction detection."](https://ieeexplore.ieee.org/document/8103330) IEEE journal of biomedical and health informatics 22, no. 5 (2017): 1434-1444.
8. Park, Yeonghyeon, Il Dong Yun, and Si-Hyuck Kang. ["Preprocessing method for performance enhancement in cnn-based stemi detection from 12-lead ecg."](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=8771175) IEEE Access 7 (2019): 99964-99977.
9. Xiao, Ran, Yuan Xu, Michele M. Pelter, David W. Mortara, and Xiao Hu. ["A deep learning approach to examine ischemic ST changes in ambulatory ECG recordings."](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5961830/) AMIA Summits on Translational Science Proceedings 2018 (2018): 256.