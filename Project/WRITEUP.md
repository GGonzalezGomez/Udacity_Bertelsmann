# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

*For **both** a VM or App Service solution for the CMS app:*
- *Analyze costs, scalability, availability, and workflow*
- *Choose the appropriate solution (VM or App Service) for deploying the app*
- *Justify your choice*

##### VMs
- VMs are generally more expensive than app services. This is obviously determined by the SKU selected, but its cost is usually higher.
- Having access to the underlying OS is a pro and a con. You have more flexibility in case you need to deploy a specific software for example, but on the other hand, you have to deploy it yourself.
- VMs are highly scalable as Azure has different load balancing options and your application may use that. Also, VMs have a wider range of SKUs available, with higher hardware values (vCPUs, memory, storage, etc).
- Regarding app CICD process, everything must be managed by the customer. So you will need to implement your own CD process.
- VMs have an advantage which is being able to tear the VM down after testing on when not needed any longer.

##### App Services
- It is usually a more cost effective solution, though you'll be paying for the service even if it is not in use.
- As a PaaS, it is maintained and managed by Azure itself. Azure is who will provide a specific service level.
- Regarding scalability, app services can be scaled up but its limit is far lower than the available VM sizes. This service is intended for lightweight applications.
- As a pro, CD process is quite simple and already available. There's a limited set of supported languages but if the app is one of them you can take full advantage of the deployment process available.

##### Suggested option
In our current case we suggest using an App Service. The main reason is that our application is lightweight, we are using one of the supported languages (python) and we do not need any specific framework/app to run our solution. This solution will also take advantage of the simple CD process.

### Assess app changes that would change your decision.

*Detail how the app and any other needs would have to change for you to change your decision in the last section.* 

The main reason to use a VM instead of an APP Service would be if we were in need of a more demanding hardware (an intensive app that required more resources). If we decided to use an specific app, for example, Tomcat or any other webapp server, we would need to use a VM. Similar if we would use one of the unsupported languages to run our application.
To sum up, scaling or an app with unsupported requirements would switch the decision.
