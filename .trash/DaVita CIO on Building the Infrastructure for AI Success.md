---
title: "DaVita CIO on Building the Infrastructure for AI Success"
source: "https://www.hcinnovationgroup.com/analytics-ai/generative-ai/article/55392766/davita-cio-on-building-the-infrastructure-for-ai-success"
author:
  - "David Raths"
published: 2026-07-22
created: 2026-07-23
description: "Madhu Narasimhan says the kidney care provider’s Center Without Walls internal ecosystem sets it up to use AI to streamline clinical workflows and provide predictive insights ..."
tags:
  - "clippings"
---
Madhu Narasimhan says the kidney care provider’s Center Without Walls internal ecosystem sets it up to use AI to streamline clinical workflows and provide predictive insights

## Key Highlights

- DaVita says its cloud-native CWOW platform provides a comprehensive, real-time view of patient data across all care points, facilitating seamless information sharing.
- AI tools developed include clinical summarization for nurses and nephrologists, hospitalization data integration, and proactive patient engagement for those on home dialysis.

![6a60ddaa2e83569365231278 Dreamstime Xl 126255023](https://img.hcinnovationgroup.com/files/base/ebm/hci/image/2026/07/6a60ddaa2e83569365231278-dreamstime_xl_126255023.png?auto=format,compress&fit=fill&fill=blur&q=45?w=250&width=250)

ID 126255023 © motortion | Dreamstime.com

Kidney care company DaVita is leveraging its homegrown Center Without Walls (CWOW) tech infrastructure to create AI tools to support nurses, nephrologists and patients. CIO Madhu Narasimhan, who came to DaVita two years ago after stints at Wells Fargo and Kaiser Permanente, spoke with *Healthcare Innovation* recently about how CWOW enhances continuity between care team members and enables AI innovations.

**Healthcare Innovation: Some health systems still have fragmented data and legacy systems that make it more challenging for them to get set up to do AI work, but is DaVita in a better position** **in terms of its infrastructure, and has it been thinking about AI for a while?**

**Narasimhan:** Yes. Historically, healthcare has had incredibly siloed, fragmented data. We have built our CWOW from a platform perspective. It’s cloud-native, and it's built for a comprehensive view of our patient interactions and care across the board. Across our 2,600 sites or clinics where we care for our patients, or in the patients’ homes, our nephrologists and caregivers all have access to the full view of the patient data. That’s a huge differentiator to begin with.

**HCI: Is there still a need for interoperability with providers outside the system, like labs or health information exchanges to get information about when your patients might see other providers?**

**Narasimhan:** We definitely do, but our patients are medically highly vulnerable. Dialysis is a life-changing thing. You show up three times a week at our centers. They have multiple co-morbidities usually. As our physicians are rounding with our patients, either in clinic or virtually, they're able to see the lab data, the HIE data, they're able to see the interaction data. I mentioned that patients come in usually three times a week and they are there for four hours. This is not a short interaction, and it generates a lot of really rich data. Basically we make sure that it's all available to care for them. So this platform is a real game-changer from that perspective, because we're able to bring everything in, and then it's fully visible across all of our caregiving points.

**HCI: How does having all of that data in that format help with creating AI tools that might help those providers and the patients even more?**

**Narasimhan:** First of all, having access to quality curated data is one of the underpinnings of getting good AI outcomes.

Here are some examples of tools we’ve created: I mentioned that our patients come in multiple times per week. Our nurses put together notes of their patient interactions for when the nephrologist is rounding in the clinic. Historically they would go into multiple tabs, look at all of the data, and then put together a summary to share with the physician. We’ve created a clinical summarization tool that allows this nurse to use AI to create that for them. There is still always clinician oversight over what is produced.

When our patients go into the hospitals, and then come back into the clinic, we get all that hospitalization data, so we've created a summarization for our nephrologists. They’re able to see the most important things quickly. We always identify where the data was sourced from, so they can click into the 80-page pdf if they want, but it raises the highlights.

Finally, some of our patients choose to do dialysis at home. We have developed AI-based tools so we can know what's happening, regardless of the site of care. We know how they're interacting based on certain indicators, and we can proactively reach out and say: “How are you doing? Are you still comfortable?” That's how we use AI to care for the patient, because we want them to know that they're not on their own.

**HCI: What approach does DaVita take to governance of AI? When someone has a new idea, like those summarization tools, how is that vetted and approved internally?**

**Narasimhan:** Ideas come from everywhere. We start with human-centered design. In the caregiving space, there is such a level of demand on their time that the last thing we want is to add cognitive overload. Our goal is to make your life easier. Then we ask if there are tools that we can bring to bear with that. We have a pretty strong governance module with legal, clinicians, and our technologists. That oversight is pretty strict.

We also have ongoing monitoring, because once you build it and you put it in, you have to continue to monitor for drift and for bias. If it’s a clinical thing, there's an extra level of oversight, just to make sure that we are being super thoughtful, and we have the right clinical views on that. We also have our own ground truths that we built. We call it the Renal Codex. It's based on our knowledge of kidney care over 30 years across all of our patients. Accuracy is not optional, and we always have a human in the loop so that clinical oversight on the final decision is always there.

**HCI: When I have spoken to some other health system about monitoring of the algorithms to watch for drift or other issues, they've said that when they just had a few algorithms, they could do it manually, but once they got up to a large number, they needed a platform at the AI orchestration level. Do you feel the need to have a platform that's looking at what the algorithms are doing in real time?**

**Narasimhan:** Yes, we do. We have periodic monitoring for drift and bias for usage-based monitoring. If a model is giving incorrect answers and that information comes back to us, that's real-time monitoring. We treat it like a production incident. We've not had that, but we would, because we have a mechanism to monitor that.

**HCI: How do you decide which things to build internally vs. seeing a great tool out there, but it's built by a startup company? What goes into that equation?**

**Narasimhan:** We start with what the human needs are first, and then, based on what is asked for, we figure out which tools we will bring to bear, and whether we will build it internally. Sometimes it's not even generative AI, sometimes it's just old-fashioned deterministic AI, because it doesn't make sense to use tokens for something that you know is highly deterministic. That decision is largely driven by what we want to get done.

For clinical tools, we are likely going to build a lot, because we have the expertise, whereas if it's something around employment, for instance, then we might just have Workday give us that.

**HCI: Are you looking at the potential of agentic AI to do patient-facing things like answering patient questions?**

**Narasimhan:** Agents can mean so many things. You start with an assistant kind of thing, or you might have bounded tasks, or truly autonomous agents, where they're orchestrating a set of actions with outcomes. We're definitely not in that third arena, because, as I said, being accurate is not optional, it is required. We are exploring agentic workflows, but they are largely single- or multi-step, but completely bounded, and it's always with human oversight. We’re starting in the usual places like the contact center, answering our teammate’s questions, that kind of thing. From a patient perspective, you can get a lot of information from consumer-grade AI, because there are no guardrails. We want to make sure that any information we provide our patients has our controls on it.

**HCI: Outside of AI, are there some other priority items that are high on your list as CIO right now?**

**Narasimhan:** I think every CIO will tell you security is one of their biggest concerns, so that continues to be top of mind as well. I think the other piece of it is making sure we understand what is real, both within AI as well as with other technologies. When is it actually adoptable? Just because it's announced doesn't mean we can actually use it. We are spending a lot of time figuring out that elapsed time between an announcement and actual usage. The other area we are very focused on is software development. How do we bring AI into that area to actually oversee that? We've had some good successes with some of the initial areas that we've looked at, both in code development as well as QA, but we've still kept the human-in-the-loop piece of it, because we've not yet found that sweet spot of not generating AI slop.

## Related

## [What Clinical Groups Told HHS They Need to Accelerate AI Adoption](https://informa.blueconic.net/rest/v2/recommendations/redirect?storeId=6d95b98e-ca7f-49e2-bf12-8862157adfdf&profileId=&itemId=55360606)

## [AI and Technology Alone Won't Fix Revenue Cycle Challenges: The Automation Paradox in RCM](https://informa.blueconic.net/rest/v2/recommendations/redirect?storeId=6d95b98e-ca7f-49e2-bf12-8862157adfdf&profileId=&itemId=55361826)

Sponsored

Sponsored