

# ![AWS Networking and Content Delivery category icon](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/images/networking-content-delivery-icon.jpg) Networking and content delivery
<a name="networking-services"></a>

 AWS offers a broad set of networking and content delivery services that provide the highest level of reliability, security, and performance in the cloud. 

Each service is described after the diagram. To help you decide which service best meets your needs, see [Choosing an AWS networking and content delivery service](https://docs.aws.amazon.com/decision-guides/latest/networking-on-aws-how-to-choose/choosing-networking-and-content-delivery-service.html). For general information, see [AWS Networking and Content Delivery](https://aws.amazon.com/products/networking/).

![Diagram showing AWS networking services](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/images/networking-services.png)


**Topics**
+ [Amazon API Gateway](#amazon-api-gateway)
+ [AWS App Mesh](#aws-app-mesh)
+ [Amazon CloudFront](#amazon-cloudfront)
+ [AWS Cloud Map](#aws-cloud-map)
+ [Direct Connect](#aws-direct-connect)
+ [Elastic Load Balancing](#elastic-load-balancing)
+ [AWS Global Accelerator](#aws-global-accelerator)
+ [Integrated Private Wireless on AWS](#integrated-private-wireless-on-aws)
+ [AWS PrivateLink](#aws-privatelink)
+ [AWS Private 5G](#aws-private5g)
+ [Amazon Route 53](#amazon-route-53)
+ [AWS Transit Gateway](#aws-transit-gateway)
+ [AWS Verified Access](#aws-verified-access)
+ [Amazon VPC](#amazon-vpc)
+ [Amazon VPC Lattice](#amazon-vpc-lattice)
+ [Site-to-Site VPN](#aws-vpn)

Return to [AWS services](amazon-web-services-cloud-platform.md).

## Amazon API Gateway
<a name="amazon-api-gateway"></a>

[Amazon API Gateway](https://aws.amazon.com/api-gateway/) is a fully managed service that makes it easy for developers to create, publish, maintain, monitor, and secure APIs at any scale. With a few clicks in the AWS Management Console, you can create an API that acts as a “front door” for applications to access data, business logic, or functionality from your back-end services, such as workloads running on Amazon EC2, code running on AWS Lambda, or any web application. Amazon API Gateway handles all the tasks involved in accepting and processing up to hundreds of thousands of concurrent API calls, including traﬃc management, authorization and access control, monitoring, and API version management.

## AWS App Mesh
<a name="aws-app-mesh"></a>

[AWS App Mesh](https://aws.amazon.com/app-mesh/) makes it easy to monitor and control [microservices](https://aws.amazon.com/microservices/) running on AWS. App Mesh standardizes how your microservices communicate, giving you end-to-end visibility and helping to ensure high-availability for your applications.

Modern applications are often composed of multiple microservices that each perform a specific function. This architecture helps to increase the availability and scalability of the application by allowing each component to scale independently based on demand, and automatically degrading functionality when a component fails instead of going offline. Each microservice interacts with all the other microservices through an API. As the number of microservices grows within an application, it becomes increasingly difficult to pinpoint the exact location of errors, re-route traffic after failures, and safely deploy code changes. Previously, this has required you to build monitoring and control logic directly into your code and redeploy your microservices every time there are changes.

AWS App Mesh makes it easy to run microservices by providing consistent visibility and network traffic controls for every microservice in an application. App Mesh removes the need to update application code to change how monitoring data is collected or traffic is routed between microservices. App Mesh configures each microservice to export monitoring data and implements consistent communications control logic across your application. This makes it easy to quickly pinpoint the exact location of errors and automatically re-route network traffic when there are failures or when code changes need to be deployed.

You can use App Mesh with [Amazon ECS](https://aws.amazon.com/ecs/) and [Amazon EKS](https://aws.amazon.com/eks/) to better run containerized microservices at scale. App Mesh uses the open source [Envoy proxy](https://www.envoyproxy.io/), making it compatible with a wide range of AWS partner and open source tools for monitoring microservices.

## Amazon CloudFront
<a name="amazon-cloudfront"></a>

[Amazon CloudFront](https://aws.amazon.com/cloudfront/) is a fast content delivery network (CDN) service that securely delivers data, videos, applications, and APIs to customers globally with low latency, high transfer speeds, all within a developer-friendly environment. CloudFront is integrated with AWS – both physical locations that are directly connected to the AWS global infrastructure, as well as other AWS services. CloudFront works seamlessly with services including AWS Shield for DDoS mitigation, Amazon S3, Elastic Load Balancing or Amazon EC2 as origins for your applications, and Lambda@Edge to run custom code closer to customers’ users and to customize the user experience. 

 You can get started with the content delivery network in minutes, using the same AWS tools that you're already familiar with: APIs, AWS Management Console, CloudFormation, CLIs, and SDKs. Amazon CDN offers a simple, pay-as-you-go pricing model with no upfront fees or required long-term contracts, and support for the CDN is included in your existing Support subscription. 

## AWS Cloud Map
<a name="aws-cloud-map"></a>

[AWS Cloud Map](https://aws.amazon.com/cloud-map/) is a cloud resource discovery service. With AWS Cloud Map, you can define custom names for your application resources, and it maintains the updated location of these dynamically changing resources. This increases your application availability because your web service always discovers the most up-to-date locations of its resources.

Modern applications are typically composed of multiple services that are accessible over an API and perform a specific function. Each service interacts with a variety of other resources such as databases, queues, object stores, and customer-defined microservices, and they also need to be able to find the location of all the infrastructure resources on which it depends, in order to function. You typically manually manage all these resource names and their locations within the application code. However, manual resource management becomes time consuming and error-prone as the number of dependent infrastructure resources increases or the number of microservices dynamically scale up and down based on traffic. You can also use third-party service discovery products, but this requires installing and managing additional software and infrastructure.

AWS Cloud Map allows you to register any application resources such as databases, queues, microservices, and other cloud resources with custom names. AWS Cloud Map then constantly checks the health of resources to make sure the location is up-to-date. The application can then query the registry for the location of the resources needed based on the application version and deployment environment.

## Direct Connect
<a name="aws-direct-connect"></a>

[Direct Connect](https://aws.amazon.com/directconnect/) makes it easy to establish a dedicated network connection from your premises to AWS. Using Direct Connect, you can establish private connectivity between AWS and your data center, office, or co-location environment, which in many cases can reduce your network costs, increase bandwidth throughput, and provide a more consistent network experience than Internet-based connections. 

 Direct Connect lets you establish a dedicated network connection between your network and one of the Direct Connect locations. Using industry standard 802.1Q virtual LANs (VLANs), this dedicated connection can be partitioned into multiple virtual interfaces. This allows you to use the same connection to access public resources, such as objects stored in Amazon S3 using public IP address space, and private resources such as EC2 instances running within a VPC using private IP address space, while maintaining network separation between the public and private environments. Virtual interfaces can be reconfigured at any time to meet your changing needs. 

## Elastic Load Balancing
<a name="elastic-load-balancing"></a>

[Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing/) (ELB) automatically distributes incoming application traffic across multiple targets, such as Amazon EC2 instances, containers, and IP addresses. It can handle the varying load of your application traffic in a single Availability Zone or across multiple Availability Zones. Elastic Load Balancing offers four types of load balancers that all feature the high availability, automatic scaling, and robust security necessary to make your applications fault tolerant. 
+ [Application Load Balancer](https://aws.amazon.com/elasticloadbalancing/features/#Details_for_Elastic_Load_Balancing_Products) is best suited for load balancing of HTTP and HTTPS traffic and provides advanced request routing targeted at the delivery of modern application architectures, including microservices and containers. Operating at the individual request level (Layer seven), Application Load Balancer routes traffic to targets within Amazon Virtual Private Cloud (Amazon VPC) based on the content of the request.
+ [Network Load Balancer](https://aws.amazon.com/elasticloadbalancing/features/#Details_for_Elastic_Load_Balancing_Products) is best suited for load balancing of TCP traffic where extreme performance is required. Operating at the connection level (Layer four), Network Load Balancer routes traffic to targets within Amazon Virtual Private Cloud (Amazon VPC) and is capable of handling millions of requests per second while maintaining ultra-low latencies. Network Load Balancer is also optimized to handle sudden and volatile traffic patterns.
+ [Gateway Load Balancer](https://aws.amazon.com/elasticloadbalancing/gateway-load-balancer/) makes it easy to deploy, scale, and run third-party virtual networking appliances. Providing load balancing and auto scaling for fleets of third-party appliances, Gateway Load Balancer is transparent to the source and destination of traffic. This capability makes it well suited for working with third-party appliances for security, network analytics, and other use cases. 
+ [Classic Load Balancer](https://aws.amazon.com/elasticloadbalancing/features/#Details_for_Elastic_Load_Balancing_Products) provides basic load balancing across multiple Amazon EC2 instances and operates at both the request level and connection level. Classic Load Balancer is intended for applications that were built within the EC2-Classic network. EC2-Classic was retired on August 15, 2022.

## AWS Global Accelerator
<a name="aws-global-accelerator"></a>

[AWS Global Accelerator](https://aws.amazon.com/global-accelerator/) is a networking service that improves the availability and performance of the applications that you offer to your global users. 

 Today, if you deliver applications to your global users over the public internet, your users might face inconsistent availability and performance as they traverse through multiple public networks to reach your application. These public networks are often congested and each hop can introduce availability and performance risk. AWS Global Accelerator uses the highly available and congestion-free AWS global network to direct internet traffic from your users to your applications on AWS, making your users’ experience more consistent. 

To improve the availability of your application, you must monitor the health of your application endpoints and route traffic only to healthy endpoints. AWS Global Accelerator improves application availability by continuously monitoring the health of your application endpoints and routing traffic to the closest healthy endpoints.

AWS Global Accelerator also makes it easier to manage your global applications by providing static IP addresses that act as a fixed entry point to your application hosted on AWS which eliminates the complexity of managing specific IP addresses for different AWS Regions and Availability Zones. AWS Global Accelerator is easy to set up, configure and manage.

## Integrated Private Wireless on AWS
<a name="integrated-private-wireless-on-aws"></a>

The Integrated Private Wireless on AWS program is designed to provide enterprises with managed and validated private wireless offerings from leading Communications Service Providers (CSPs). The offerings integrate CSPs’ private 5G and 4G LTE wireless networks with AWS services across [AWS Regions](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/), [AWS Local Zones](https://aws.amazon.com/about-aws/global-infrastructure/localzones/), [AWS Outposts](https://aws.amazon.com/outposts/), and [AWS Snow Family](https://aws.amazon.com/snow/). AWS Telco Solutions Architects technically validate the offerings for their sound architecture, and adherence to AWS best practices. Telecom companies deliver, operate, and support the offerings. 

The program also uses the rich expertise of validated global AWS Independent Software Vendor (ISV) partners to accelerate the time-to-value for private wireless deployment. Integrated Private Wireless on AWS removes the long planning cycles and complex integrations usually required to set up and scale a private wireless network. You can now deploy a secure, reliable, and low-latency private wireless network to power AI/ML and IoT workloads at the edge and at scale.

## AWS PrivateLink
<a name="aws-privatelink"></a>

[AWS PrivateLink](https://aws.amazon.com/privatelink/) simplifies the security of data shared with cloud-based applications by eliminating the exposure of data to the public Internet. AWS PrivateLink provides private connectivity between VPCs, AWS services, and on-premises applications, securely on the Amazon network. AWS PrivateLink makes it easy to connect services across different accounts and VPCs to significantly simplify the network architecture. 

## AWS Private 5G
<a name="aws-private5g"></a>

[AWS Private 5G](https://aws.amazon.com/private5g/) offers an easy way to use cellular technology to augment your current network. This can help you increase reliability, extend coverage, or allow a new class of workloads, such as factory automation, autonomous robotics, and advanced augmented and virtual reality (AR/VR). You will receive all the Private 5G hardware (including SIM cards) and software you need to deploy your private cellular network and connect devices to your applications. 

With a few clicks in the AWS Management Console, deploy a private cellular network that meets your connectivity requirements. Start by specifying the connectivity requirements for the desired location, the number of devices you want to connect, and the geographic area they will cover. AWS will deliver pre-integrated hardware and software components (from both AWS and our AWS Partners) that meet the enterprise connectivity requirements of your private network. AWS delivers and maintains the small cell radio units, servers, 5G core, radio access network (RAN) software, and SIM cards required to set up a private 5G network and connect devices. Once the equipment is powered on, AWS automatically configures and deploys the cellular network. All you need to do is insert the SIM cards into your devices. 

AWS Private 5G is also integrated with AWS Identity and Access Management (IAM), which helps you securely access and manage AWS services and resources, including all devices connected to your Private 5G network. Private 5G manages and maintains all the software and hardware components to deliver reliable, predictable network behavior and on-demand scaling to accommodate any number of devices and sensors.

## Amazon Route 53
<a name="amazon-route-53"></a>

[Amazon Route 53](https://aws.amazon.com/route53/) is a highly available and scalable cloud Domain Name System (DNS) web service. It is designed to give developers and businesses an extremely reliable and cost-effective way to route users to internet applications by translating human-readable names, such as `www.example.com`, into the numeric IP addresses, such as `192.0.2.1`, that computers use to connect to each other. Amazon Route 53 is fully compliant with IPv6 as well. 

Amazon Route 53 effectively connects user requests to infrastructure running in AWS—such as EC2 instances, elastic load balancers, or Amazon S3 buckets—and can also be used to route users to infrastructure outside of AWS. You can use Amazon Route 53 to configure DNS health checks to route traffic to healthy endpoints or to independently monitor the health of your application and its endpoints.

Amazon Route 53 traffic flow makes it easy for you to manage traffic globally through a variety of routing types, including latency-based routing, Geo DNS, and weighted round robin—all of which can be combined with DNS Failover in order to enable a variety of low-latency, fault-tolerant architectures. Using Amazon Route 53 traffic flow’s simple visual editor, you can easily manage how your end users are routed to your application’s endpoints—whether in a single AWS Region or distributed around the globe. Amazon Route 53 also offers Domain Name Registration—you can purchase and manage domain names such as `example.com` and Amazon Route 53 will automatically configure DNS settings for your domains. 

## AWS Transit Gateway
<a name="aws-transit-gateway"></a>

[AWS Transit Gateway](https://aws.amazon.com/transit-gateway/) is a service that enables customers to connect their Amazon Virtual Private Clouds (VPCs) and their on-premises networks to a single gateway. As you grow the number of workloads running on AWS, you need to be able to scale your networks across multiple accounts and Amazon VPCs to keep up with the growth. Today, you can connect pairs of Amazon VPCs using peering. However, managing point-to-point connectivity across many Amazon VPCs, without the ability to centrally manage the connectivity policies, can be operationally costly and cumbersome. For on-premises connectivity, you need to attach your Site-to-Site VPN to each individual Amazon VPC. This solution can be time consuming to build and hard to manage when the number of VPCs grows into the hundreds.

With AWS Transit Gateway, you only have to create and manage a single connection from the central gateway in to each Amazon VPC, on-premises data center, or remote office across your network. Transit Gateway acts as a hub that controls how traffic is routed among all the connected networks which act like spokes. This hub and spoke model significantly simplifies management and reduces operational costs because each network only has to connect to the Transit Gateway and not to every other network. Any new VPC is simply connected to the Transit Gateway and is then automatically available to every other network that is connected to the Transit Gateway. This ease of connectivity makes it easy to scale your network as you grow.

## AWS Verified Access
<a name="aws-verified-access"></a>

[AWS Verified Access](https://aws.amazon.com/verified-access/) provides corporate users secure access to your applications without using a virtual private network (VPN). Based on AWS Zero Trust principles, Verified Access evaluates each application request in real time to help ensure that users can only access your applications after they meet speciﬁed security requirements. You can group applications, or deﬁne unique access policies for each application, with conditions based on user identity and device posture data.

## Amazon VPC
<a name="amazon-vpc"></a>

[Amazon Virtual Private Cloud](https://aws.amazon.com/vpc/) (Amazon VPC) lets you provision a logically isolated section of the AWS Cloud where you can launch AWS resources in a virtual network that you define. You have complete control over your virtual networking environment, including selection of your own IP address range, creation of subnets, and configuration of route tables and network gateways. You can use both IPv4 and IPv6 in your VPC for secure and easy access to resources and applications. 

 You can easily customize the network configuration for your VPC. For example, you can create a public-facing subnet for your web servers that has access to the Internet, and place your backend systems, such as databases or application servers, in a private-facing subnet with no Internet access. You can leverage multiple layers of security (including security groups and network access control lists) to help control access to EC2 instances in each subnet. 

 Additionally, you can create a hardware virtual private network (VPN) connection between your corporate data center and your VPC and leverage the AWS Cloud as an extension of your corporate data center. 

## Amazon VPC Lattice
<a name="amazon-vpc-lattice"></a>

[Amazon VPC Lattice](https://aws.amazon.com/vpc/lattice/) provides fully managed support for service-to-service connectivity and communication. With VPC Lattice, you can use policies to define network traffic management, access, and monitoring to connect compute services in a simplified and secure way across instances, containers, and serverless applications. 

## Site-to-Site VPN
<a name="aws-vpn"></a>

[AWS Virtual Private Network](https://aws.amazon.com/vpn/) (Site-to-Site VPN) solutions establish secure connections between your on-premises networks, remote offices, client devices, and the AWS global network. Site-to-Site VPN is comprised of two services: AWS Site-to-Site VPN and AWS Client VPN. Each service provides a highly-available, managed, and elastic cloud VPN solution to protect your network traffic.

AWS Site-to-Site VPN creates encrypted tunnels between your network and your Amazon Virtual Private Clouds or AWS Transit Gateways. For managing remote access, AWS Client VPN connects your users to AWS or on-premises resources using a VPN software client.

Return to [AWS services](amazon-web-services-cloud-platform.md).