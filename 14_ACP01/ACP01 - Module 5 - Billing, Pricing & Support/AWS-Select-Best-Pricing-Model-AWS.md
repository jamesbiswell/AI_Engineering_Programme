

# Select the best pricing model
<a name="select-the-best-pricing-model"></a>

 **Perform workload cost modeling:** Consider the requirements of the workload components and understand the potential pricing models. Define the availability requirement of the component. Determine if there are multiple independent resources that perform the function in the workload, and what the workload requirements are over time. Compare the cost of the resources using the default On-Demand pricing model and other applicable models. Factor in any potential changes in resources or workload components. 

 **Perform regular account level analysis:** Performing regular cost modeling ensures that opportunities to optimize across multiple workloads can be implemented. For example, if multiple workloads use On-Demand, at an aggregate level, the risk of change is lower, and implementing a commitment-based discount will achieve a lower overall cost. It is recommended to perform analysis in regular cycles of two weeks to one month. This analysis allows you to make small adjustment purchases, so the coverage of your pricing models continues to evolve with your changing workloads and their components. 

Use the [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) recommendations tool to find opportunities for commitment discounts. 

To find opportunities for Spot workloads, use an hourly view of your overall usage, and look for regular periods of changing usage or elasticity. 

 **Pricing models:** AWS has multiple [pricing models](https://aws.amazon.com/pricing/) that allow you to pay for your resources in the most cost-effective way that suits your organization’s needs. The following section describes each purchasing model: 
+ On-Demand Instances 
+ Spot Instances 
+ Commitment discounts - Savings Plans 
+ Commitment discounts - Reserved Instances/Capacity 
+ Geographic selection 
+ Third-party agreements and pricing 

 **On-Demand Instances:** This is the default, pay as you go pricing model. When you use resources (for example, EC2 instances or services such as DynamoDB on demand) you pay a flat rate, and you have no long-term commitments. You can increase or decrease the capacity of your resources or services based on the demands of your application. On-Demand has an hourly rate, but depending on the service, can be billed in increments of one second (for example Amazon RDS, or Linux EC2 instances). On demand is recommended for applications with short-term workloads (for example, a four-month project), that spike periodically, or unpredictable workloads that can’t be interrupted. On demand is also suitable for workloads, such as pre-production environments, which require uninterrupted runtimes, but do not run long enough for a commitment discount (Savings Plans or Reserved Instances). 

 **Spot Instances:** A [Spot Instance](https://aws.amazon.com/ec2/spot/) is spare Amazon EC2 compute capacity available at discounts of up to 90% off On-Demand prices with no long-term commitment required. With Spot Instances, you can significantly reduce the cost of running your applications or scale your application’s compute capacity for the same budget. Unlike On-Demand, Spot Instances can be interrupted with a 2-minute warning if Amazon EC2 needs the capacity back, or the Spot Instance price exceeds your configured price. On average, Spot Instances are interrupted less than 5% of the time. 

 Spot Instances are ideal when there is a queue or buffer in place, or where there are multiple resources working independently to process the requests (for example, Hadoop data processing). Typically these workloads are fault-tolerant, stateless, and flexible, such as batch processing, big data and analytics, containerized environments, and high performance computing (HPC). Non-critical workloads such as test and development environments are also candidates for Spot. 

 Spot Instances are also integrated into multiple AWS services, such as Amazon EC2 Auto Scaling groups, Amazon EMR, Amazon Elastic Container Service (Amazon ECS), and AWS Batch. 

 When a Spot Instance needs to be reclaimed, Amazon EC2 sends a two-minute warning via a Spot Instance interruption notice delivered through CloudWatch Events, as well as in the instance metadata. During that two-minute period, your application can use the time to save its state, drain running containers, upload final log files, or remove itself from a load balancer. At the end of the two minutes, you have the option to hibernate, stop, or terminate the Spot Instance. 

 Consider the following best practices when adopting Spot Instances in your workloads: 
+  **Be flexible across as many instance types as possible:** Be flexible in both the family and size of the instance type, to improve the likelihood of fulfilling your target capacity requirements, obtain the lowest possible cost, and minimize the impact of interruptions. 
+  **Be flexible about where your workload will run:** Available capacity can vary by Availability Zone. This improves the likelihood of fulfilling your target capacity by tapping into multiple spare capacity pools, and provides the lowest possible cost. 
+  **Design for continuity:** Design your workloads for statelessness and fault-tolerance, so that if some of your EC2 capacity gets interrupted, it will not have impact on the availability or performance of the workload. 
+  We recommend using Spot Instances in combination with On-Demand and Savings Plans/Reserved Instances to maximize workload cost optimization with performance. 

 **Commitment discounts – Savings Plans:** AWS provides a number of ways for you to reduce your costs by reserving or committing to use a certain amount of resources, and receiving a discounted rate for your resources. A [Savings Plan](https://aws.amazon.com/savingsplans/) allows you to make an hourly spend commitment for one or three years, and receive discounted pricing across your resources. Savings Plans provide discounts for AWS Compute services such as Amazon EC2, AWS Fargate, and AWS Lambda. When you make the commitment, you pay that commitment amount every hour, and it is subtracted from your On-Demand usage at the discount rate. For example, you commit to $50 an hour, and have $150 an hour of On-Demand usage. Considering the Savings Plans pricing, your specific usage has a discount rate of 50%. So, your $50 commitment covers $100 of On-Demand usage. You will pay $50 (commitment) and $50 of remaining On-Demand usage. 

 [Compute Savings Plans](https://aws.amazon.com/savingsplans/pricing/) are the most flexible and provide a discount of up to 66%. They automatically apply across Availability Zones, instance size, instance family, operating system, tenancy, Region, and compute service. 

 [Instance Savings Plans](https://aws.amazon.com/savingsplans/pricing/) have less flexibility but provide a higher discount rate (up to 72%). They automatically apply across Availability Zones, instance size, operating system, and tenancy. 

 There are three payment options: 
+  **No upfront payment:** There is no upfront payment; you then pay a reduced hourly rate each month for the total hours in the month. 
+  **Partial upfront payment:** Provides a higher discount rate than No upfront. Part of the usage is paid up front; you then pay a smaller reduced hourly rate each month for the total hours in the month. 
+  **All upfront payment:** Usage for the entire period is paid up front, and no other costs are incurred for the remainder of the term for usage that is covered by the commitment. 

 You can apply any combination of these three purchasing options across your workloads. 

 Savings plans apply first to the usage in the account they are purchased in, from the highest discount percentage to the lowest, then they apply to the consolidated usage across all other accounts, from the highest discount percentage to the lowest. 

 It is recommended to purchase all Savings Plans in an account with no usage or resources, such as the management account. This ensures that the Savings Plan applies to the highest discount rates across all of your usage, maximizing the discount amount. 

 Workloads and usage typically change over time. It is recommended to continually purchase small amounts of Savings Plans commitment over time. This ensures that you maintain high levels of coverage to maximize your discounts, and your plans closely match your workload and organization requirements at all times. 

 Do not set a target coverage in your accounts, due to the variability of discount that is possible. Low coverage does not necessarily indicate high potential savings. You may have a low coverage in your account, but if your usage is made up of small instances, with a licensed operating system, the potential saving could be as low as a few percent. Instead, track and monitor the potential savings available in the Savings Plan recommendation tool. Frequently review the Savings Plans recommendations in Cost Explorer (perform regular analysis) and continue to purchase commitments until the estimated savings are below the required discount for the organization. For example, track and monitor that your potential discounts remained below 20%, if it goes above that a purchase must be made. 

 Monitor the utilization and coverage, but only to detect changes. Do not aim for a specific utilization percent, or coverage percent, as this does not necessarily scale with savings. Ensure that a purchase of Savings Plans results in an increase in coverage, and if there are decreases in coverage or utilization ensure they are quantified and known. For example, you migrate a workload resource to a newer instance type, which reduces utilization of an existing plan, but the performance benefit outweighs the saving reduction. 

 **Commitment discounts – Reserved Instances/Commitment:** Similar to Savings Plans, [Reserved Instances](https://aws.amazon.com/ec2/pricing/reserved-instances/) (RI) offer discounts up to 72% for a commitment to running a minimum amount of resources. Reserved Instances are available for Amazon RDS, Amazon OpenSearch Service, Amazon ElastiCache, Amazon Redshift, and DynamoDB. Amazon CloudFront and AWS Elemental MediaConvert also provide discounts when you make minimum usage commitments. Reserved Instances are currently available for Amazon EC2, however Savings Plans offer the same discount levels with increased flexibility and no management overhead. 

Reserved Instances offer the same pricing options of no upfront, partial upfront, and all upfront, and the same terms of one or three years. 

Reserved Instances can be purchased in a Region or a specific Availability Zone. They provide a capacity reservation when purchased in an Availability Zone. 

Amazon EC2 features convertible RIs, however, Savings Plans should be used for all EC2 instances due to increased flexibility and reduced operational costs. 

 The same process and metrics should be used to track and make purchases of Reserved Instances. It is recommended to not track coverage of RIs across your accounts. It is also recommended that utilization percentage is not monitored or tracked, instead view the utilization report in Cost Explorer, and use net savings column in the table. If the net savings is a significantly large negative amount, you must take action to remediate the unused RI. 

 **EC2 Fleet:** [EC2 Fleet](https://aws.amazon.com/about-aws/whats-new/2018/04/introducing-amazon-ec2-fleet/) is a feature that allows you to define a target compute capacity, and then specify the instance types and the balance of On-Demand and Spot Instances for the fleet. EC2 Fleet will automatically launch the lowest price combination of resources to meet the defined capacity. 

 **Geographic selection:** When you architect your solutions, a best practice is to seek to place computing resources closer to users to provide lower latency and strong data sovereignty. For global audiences, you should use multiple locations to meet these needs. You should select the geographic location that minimizes your costs. 

 The AWS Cloud infrastructure is built around [Regions and Availability Zones](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html). A Region is a physical location in the world where we have multiple Availability Zones. Availability Zones consist of one or more discrete data centers, each with redundant power, networking, and connectivity, housed in separate facilities. 

 Each AWS Region operates within local market conditions, and resource pricing is different in each Region. Choose a specific Region to operate a component of or your entire solution so that you can run at the lowest possible price globally. You can use the AWS Simple Monthly Calculator to estimate the costs of your workload in various Regions. 

 **Third-party agreements and pricing:** When you use third-party solutions or services in the cloud, it is important that the pricing structures are aligned to Cost Optimization outcomes. Pricing should scale with the outcomes and value it provides. An example of this is software that takes a percentage of savings it provides, the more you save (outcome) the more it charges. Agreements that scale with your bill are typically not aligned to Cost Optimization, unless they provide outcomes for every part of your specific bill. For example, a solution that provides recommendations for Amazon EC2 and charges a percentage of your entire bill will increase if you use other services for which it provides no benefit. Another example is a managed service that is charged at a percentage of the cost of resources that are managed. A larger instance size may not necessarily require more management effort, but will be charged more. Ensure that these service pricing arrangements include a cost optimization program or features in their service to drive efficiency. 

**Topics**
+ [COST07-BP01 Perform pricing model analysis](cost_pricing_model_analysis.md)
+ [COST07-BP02 Choose Regions based on cost](cost_pricing_model_region_cost.md)
+ [COST07-BP03 Select third-party agreements with cost-efficient terms](cost_pricing_model_third_party.md)
+ [COST07-BP04 Implement pricing models for all components of this workload](cost_pricing_model_implement_models.md)
+ [COST07-BP05 Perform pricing model analysis at the management account level](cost_pricing_model_master_analysis.md)