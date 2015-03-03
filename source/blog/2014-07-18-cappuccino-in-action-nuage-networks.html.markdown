---
title: Cappuccino in action
date: '2014-07-18'
author: Antoine Mercadal
tags:
- nuagenetworks
- sdn
- showcase
---

> This is the first in a series of articles where the community can showcase what they are doing with Cappuccino.

In this blog post I will briefly explain what we are doing here at Nuage Networks, why we chose Cappuccino, why we love it, and what we’ve done with it.

[Nuage Networks](http://www.nuagenetworks.net) is an Alcatel-Lucent venture, a start-up operating as part of a global company. Our Virtualized Services Platform (VSP) is a [Software Defined Network](http://en.wikipedia.org/wiki/Software-defined_networking) solution. Of late, SDN is quite an exciting (and also over-hyped) technology in the world of networking because it brings the power and simplicity of server virtualization to datacenter networks. Our VSP is a policy driven networking configuration tool that exposes everything it can do over ReST APIs and a user interface that uses this API.

Of course, our UI — named VSP Architect — is built with Cappuccino.


#### Architect

I'm in charge of building that UI, and as an active developer and a lover of Cappuccino, it was pretty clear that to me it would be a perfect fit. Cappuccino is exactly meant for these kinds of projects. Big fat projects, packed with features and a lot of complex interactions. Nuage is a growing company. When I joined, we were five people. Today we are more than one hundred and the VSP Architect code base is around 280,000 lines of code. And yet, we are still only a team of two working on the UI.

[![](/img/cpo-uploads/2014/07/architect-domain.png)](/img/cpo-uploads/2014/07/architect-domain.png)

One of the most interesting aspects of Cappuccino is that you can focus on your features. It also allows you to create strong code separation, and when you need something new, you can develop a third party framework. We always do this while keeping in mind that everything must be generic, and not only suit our specific current needs. This approach forces us to produce good, clear and maintainable code.

Being able to use Xcode is also wonderful. It saves hours of work. Our low level framework is completely outlets and actions enabled, and adding new managed objects is often simply a matter of setting correct runtime attributes, and linking our outlets in Interface Builder. If tomorrow we have a new API (for instance to manage a new unicorn object), it would take 10 minutes (literally) to have fully working CRUD operations, filtering, pagination, push events management, live input validation, permission enforcement, and so much more.

#### GraphCappuccino

GraphCappuccino is a framework we are developing internally (we will certainly open source it at some point) that provides a host of different drawing components:

- `NUChartView` bar, lines, pie charts that can handle thousands of points in a few milliseconds
- `NUTreeView` with completely configurable behavior, search, expand and collapse, drag and drop and much more
- `NUGraphView` like the tree view — but wait — it's a graph!
- `NUConnector` and `NUWire` that allows you to draw lines to make connections between any variety of views

[![](/img/cpo-uploads/2014/07/graphcappucino-charts.png)](/img/cpo-uploads/2014/07/graphcappucino-charts.png)

[![](/img/cpo-uploads/2014/07/architect-acls.png)](/img/cpo-uploads/2014/07/architect-acls.png)


#### Flat Theme

NUAristo is our internal flat version of Aristo. The biggest advantage of it — in addition of looking awesome — is that it's ridiculously small. From several MB, we shrank it to a few KB. It is also tailored and reduced to only provide resources for the controls we use. So we can make it even smaller. It also has a concept of “skins" in which we declare what is blue, red, green, yellow, and so on and can use that in the theme and across the entire application. So when we decide to make that blue a little bit brighter, we just update the skin file. Alternatives color sets are also supported for colorblind people.

[![](/img/cpo-uploads/2014/07/NUAristo.png)](/img/cpo-uploads/2014/07/NUAristo.png)


#### Testing

The biggest challenge we had with Cappuccino was automated testing. The only available testing framework around these days is [Cucapp](https://github.com/cappuccino/cucapp), but when started using it, it looked like an abandoned house. But good news everyone, we improved it. We made it modular, and more easy to use. It has also been modified to send actual events instead of using high level methods on controls. That way, we ensure that what you test with your fingers works the same in Cucapp and vice versa.

Our changes in Cucapp have been released a few days ago (another blog post will follow to explain all the new features).

For everything related to unit testing, we use the standard [OJTest](https://github.com/cappuccino/ojtest) that comes with Cappuccino.


#### Conclusion

Nuage Networks and our VSP Architect are living proof that Cappuccino can help you build very complex applications, with style, even in the context of a big company working on huge products. Cappuccino is incredibly powerful and very stable. Almost without exception, it works just like you would expect. All Cocoa developers around know this, but, hell! It's running in a browser!
