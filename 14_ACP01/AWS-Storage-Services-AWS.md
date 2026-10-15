

# ![AWS Storage category icon](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/images/storage-icon.jpg) Storage
<a name="storage-services"></a>

AWS provides a broad portfolio of storage services with deep functionality for storing, accessing, protecting, and analyzing your data. 

Each service is described after the diagram. To help you decide which service best meets your needs, see [Choosing an AWS storage service](https://docs.aws.amazon.com/decision-guides/latest/storage-on-aws-how-to-choose/choosing-aws-storage-service.html). For general information, see [Cloud Storage on AWS](https://aws.amazon.com/products/storage/).

![Diagram showing AWS storage services](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/images/storage-services.png)


**Topics**
+ [AWS Backup](#aws-backup)
+ [Amazon Elastic Block Store](#amazon-elastic-block-store)
+ [AWS Elastic Disaster Recovery](#aws-elastic-disaster-recovery)
+ [Amazon Elastic File System](#amazon-elastic-file-system)
+ [Amazon File Cache](#amazon-file-cache)
+ [Amazon FSx for Lustre](#amazon-fsx-lustre)
+ [Amazon FSx for NetApp ONTAP](#amazon-fsx-netapp-ontap)
+ [Amazon FSx for OpenZFS](#amazon-fsx-openzfs)
+ [Amazon FSx for Windows File Server](#amazon-fsx-windows)
+ [Amazon Simple Storage Service](#amazon-s3)
+ [AWS Storage Gateway](#aws-storage-gateway)

Return to [AWS services](amazon-web-services-cloud-platform.md).

## AWS Backup
<a name="aws-backup"></a>

[AWS Backup](https://aws.amazon.com/backup/) enables you to centralize and automate data protection across AWS services. AWS Backup offers a cost-effective, fully managed, policy-based service that further simplifies data protection at scale. AWS Backup also helps you support your regulatory compliance or business policies for data protection. Together with AWS Organizations, AWS Backup enables you to centrally deploy data protection policies to configure, manage, and govern your backup activity across your organization’s AWS accounts and resources, including Amazon Elastic Compute Cloud (Amazon EC2) instances, Amazon Elastic Block Store (Amazon EBS) volumes, Amazon Relational Database Service (Amazon RDS) databases (including Amazon Aurora clusters), Amazon DynamoDB tables, Amazon Elastic File System (Amazon EFS) file systems, Amazon FSx for Lustre file systems, Amazon FSx for Windows File Server file systems, and AWS Storage Gateway volumes.

## Amazon Elastic Block Store
<a name="amazon-elastic-block-store"></a>

[Amazon Elastic Block Store](https://aws.amazon.com/ebs/) (Amazon EBS) provides persistent block storage volumes for use with Amazon EC2 instances in the AWS Cloud. Each Amazon EBS volume is automatically replicated within its Availability Zone to protect you from component failure, offering high availability and durability. Amazon EBS volumes offer the consistent and low-latency performance needed to run your workloads. With Amazon EBS, you can scale your usage up or down within minutes—all while paying a low price for only what you provision. 

## AWS Elastic Disaster Recovery
<a name="aws-elastic-disaster-recovery"></a>

[AWS Elastic Disaster Recovery](https://aws.amazon.com/disaster-recovery/) (Elastic Disaster Recovery) minimizes downtime and data loss with fast, reliable recovery of on-premises and cloud-based applications using affordable storage, minimal compute, and point-in-time recovery. You can configure replication and launch settings, monitor data replication, and launch instances for drills or recovery. 

Set up Elastic Disaster Recovery on your source servers to initiate secure data replication. Your data is replicated to a staging area subnet in your AWS account, in the AWS Region that you select. You can perform non-disruptive tests to confirm that implementation is complete. During normal operation, maintain readiness by monitoring replication and periodically performing non-disruptive recovery and failback drills. 

If you must replicate to the AWS China Regions or perform replication and recovery into AWS Outposts, use [CloudEndure Disaster Recovery](https://aws.amazon.com/marketplace/pp/prodview-zhtwhroiq2luq) available in the AWS Marketplace.

## Amazon Elastic File System
<a name="amazon-elastic-file-system"></a>

[Amazon Elastic File System (Amazon EFS)](https://aws.amazon.com/efs/) provides a simple, scalable, elastic file system for Linux-based workloads for use with AWS Cloud services and on-premises resources. It is built to scale on demand to petabytes without disrupting applications, growing and shrinking automatically as you add and remove files, so your applications have the storage they need – when they need it. It is designed to provide massively parallel shared access to thousands of Amazon EC2 instances, enabling your applications to achieve high levels of aggregate throughput and IOPS with consistent low latencies. Amazon EFS is a fully managed service that requires no changes to your existing applications and tools, providing access through a standard file system interface for seamless integration. Amazon EFS is a regional service storing data within and across multiple Availability Zones (AZs) for high availability and durability. You can access your file systems across Availability Zones and AWS Regions and share files between thousands of Amazon EC2 instances and on-premises servers via Direct Connect or Site-to-Site VPN. 

 Amazon EFS is well suited to support a broad spectrum of use cases from highly parallelized, scale-out workloads that require the highest possible throughput to single-threaded, latency-sensitive workloads. Use cases such as lift-and-shift enterprise applications, big data analytics, web serving and content management, application development and testing, media and entertainment workflows, database backups, and container storage. 

For long-lived data that is accessed only a few times a year or less, consider Amazon EFS Archive, a cost-effective way to retain even your coldest data so that it's always available to power new business insights. Amazon EFS Archive supports the same intelligent tiering experience as existing EFS storage classes. This means that you can combine the sub-millisecond SSD latencies of Amazon EFS Standard for your active frequently-accessed data with the lower costs of Amazon EFS IA and Amazon EFS Archive for your colder data. 

## Amazon File Cache
<a name="amazon-file-cache"></a>

[Amazon File Cache](https://aws.amazon.com/filecache/) is a fully managed high-speed cache on AWS that makes it easier to process file data, regardless of where the data is stored. Amazon File Cache serves as temporary, high-performance storage for data in on-premises file systems, or in file systems or object stores on AWS. The service allows you to make dispersed datasets available to file-based applications on AWS with a unified view and high speeds. You can link the cache to multiple NFS—including on-premises and in-cloud—or [Amazon Simple Storage Service](https://aws.amazon.com/s3/) (Amazon S3) buckets, providing a unified view of and fast access to your data spanning on-premises and multiple AWS Regions. The cache provides read and write data access to compute workloads on AWS with sub-millisecond latencies, up to hundreds of GB/s of throughput, and up to millions of [IOPS](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-io-characteristics.html). 

## Amazon FSx for Lustre
<a name="amazon-fsx-lustre"></a>

[Amazon FSx for Lustre](https://aws.amazon.com/fsx/lustre/) is a fully managed file system that is optimized for compute-intensive workloads, such as high performance computing, machine learning, and media data processing workflows. Many of these applications require the high-performance and low latencies of scale-out, parallel file systems. Operating these file systems typically requires specialized expertise and administrative overhead, requiring you to provision storage servers and tune complex performance parameters. With Amazon FSx, you can launch and run a Lustre file system that can process massive data sets at up to hundreds of gigabytes per second of throughput, millions of IOPS, and sub-millisecond latencies. 

 Amazon FSx for Lustre is seamlessly integrated with Amazon S3, making it easy to link your long-term data sets with your high performance file systems to run compute-intensive workloads. You can automatically copy data from S3 to Amazon FSx for Lustre, run your workloads, and then write results back to S3. Amazon FSx for Lustre also enables you to burst your compute-intensive workloads from on-premises to AWS by allowing you to access your FSx file system over Amazon Direct Connect or VPN. Amazon FSx for Lustre helps you cost-optimize your storage for compute-intensive workloads: It provides cheap and performant non-replicated storage for processing data, with your long-term data stored durably in Amazon S3 or other low-cost data stores. With Amazon FSx, you pay for only the resources you use. There are no minimum commitments, upfront hardware or software costs, or additional fees. 

## Amazon FSx for NetApp ONTAP
<a name="amazon-fsx-netapp-ontap"></a>

[Amazon FSx for NetApp ONTAP](https://aws.amazon.com/fsx/netapp-ontap/) offers the first complete, fully managed NetApp file system available in the cloud making it easy for you to migrate or extend existing applications to AWS without changing code or how you manage your data . Built on NetApp ONTAP, Amazon FSx for NetApp ONTAP provides the familiar features, performance, capabilities, and APIs of NetApp file systems with the agility, scalability, and simplicity of a fully managed AWS service.

Amazon FSx for NetApp ONTAP offers high-performance file storage that is broadly accessible from Linux, Windows, and macOS compute instances via the industry-standard NFS, SMB, and iSCSI protocols. With Amazon FSx for NetApp ONTAP, you get low-cost, fully elastic storage capacity with support for compression and deduplication to help you further reduce storage costs. Amazon FSx for NetApp ONTAP file systems can be deployed and managed using the AWS Management Console or NetApp Cloud Manager for seamless set up and administration.

## Amazon FSx for OpenZFS
<a name="amazon-fsx-openzfs"></a>

[Amazon FSx for OpenZFS](https://aws.amazon.com/fsx/openzfs/) is a fully managed file storage service that lets you launch, run, and scale fully managed file systems built on the open-source OpenZFS file system. Amazon FSx for OpenZFS makes it easy to migrate your on-premises file servers—without changing your applications or how you manage data—and build new high-performance, data-driven applications in the cloud.

Amazon FSx for OpenZFS offers the familiar features, performance, and capabilities of OpenZFS file systems with the agility, scalability, and simplicity of a fully managed AWS service.

## Amazon FSx for Windows File Server
<a name="amazon-fsx-windows"></a>

[Amazon FSx for Windows File Server](https://aws.amazon.com/fsx/windows/) provides a fully managed native Microsoft Windows file system so you can easily move your Windows-based applications that require file storage to AWS. Built on Windows Server, Amazon FSx provides shared file storage with the compatibility and features that your Windows-based applications rely on, including full support for the SMB protocol and Windows NTFS, Active Directory (AD) integration, and Distributed File System (DFS). Amazon FSx uses SSD storage to provide the fast performance your Windows applications and users expect, with high levels of throughput and IOPS, and consistent sub-millisecond latencies. This compatibility and performance is particularly important when moving workloads that require Windows shared file storage, such as CRM, ERP, and .NET applications, as well as home directories. 

 With Amazon FSx, you can launch highly durable and available Windows file systems that can be accessed from up to thousands of compute instances using the industry-standard SMB protocol. Amazon FSx eliminates the typical administrative overhead of managing Windows file servers. You pay for only the resources used, with no upfront costs, minimum commitments, or additional fees. 

## Amazon Simple Storage Service
<a name="amazon-s3"></a>

[Amazon Simple Storage Service](https://aws.amazon.com/s3/) (Amazon S3) is an object storage service that offers industry-leading scalability, data availability, security, and performance. This means customers of all sizes and industries can use it to store and protect any amount of data for a range of use cases, such as websites, mobile applications, backup and restore, archive, enterprise applications, IoT devices, and big data analytics. Amazon S3 provides easy-to-use management features so you can organize your data and configure finely-tuned access controls to meet your specific business, organizational, and compliance requirements. Amazon S3 is designed for 99.999999999% (11 9s) of durability, and stores data for millions of applications for companies all around the world. 

[Amazon S3 storage classes](https://aws.amazon.com/s3/storage-classes/) are a range of storage classes that you can choose from based on the data access, resiliency, and cost requirements of your workloads. S3 storage classes are purpose-built to provide the lowest cost storage for different access patterns. S3 storage classes are ideal for virtually any use case, including those with demanding performance needs, data residency requirements, unknown or changing access patterns, or archival storage.

The S3 storage classes include:
+ **S3 Intelligent-Tiering** for automatic cost savings for data with unknown or changing access patterns
+ **S3 Standard** for frequently accessed data
+ **S3 Express One Zone** for your most frequently accessed data
+ **S3 Standard-Infrequent Access (S3 Standard-IA)** and **S3 One Zone-Infrequent Access (S3 One Zone-IA)** for less frequently accessed data
+ **S3 Glacier Instant Retrieval** for archive data that needs immediate access
+ **S3 Glacier Flexible Retrieval** (formerly Amazon Glacier) for rarely accessed long-term data that does not require immediate access
+ **Amazon Glacier Deep Archive (Amazon Glacier Deep Archive)** for long-term archive and digital preservation with retrieval in hours at the lowest cost storage in the cloud

If you have data residency requirements that can’t be met by an existing AWS Region, you can use the **S3 Outposts** storage class to store your S3 data on premises. Amazon S3 also offers capabilities to manage your data throughout its lifecycle. Once an S3 Lifecycle policy is set, your data will automatically transfer to a different storage class without any changes to your application. For more information, refer to the [Amazon S3 storage classes overview info graphic](https://aws.amazon.com/s3/storage-classes-infographic/).

You can use [S3 Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html) to help prevent S3 objects from being deleted or overwritten for a fixed amount of time, or indefinitely. Object Lock can help you to meet regulatory requirements that require WORM (write-once-read-many) storage, or to simply add another layer of protection against object changes or deletion.

## AWS Storage Gateway
<a name="aws-storage-gateway"></a>

 The [AWS Storage Gateway](https://aws.amazon.com/storagegateway/) is a hybrid storage service that allows your on-premises applications to seamlessly use AWS cloud storage. You can use the service for backup and archiving, disaster recovery, cloud data processing, storage tiering, and migration. Your applications connect to the service through a virtual machine or hardware gateway appliance using standard storage protocols, such as NFS, SMB and iSCSI. The gateway connects to AWS storage services, such as Amazon S3, Amazon Glacier, and Amazon EBS, and Amazon FSx for Windows File Server, providing storage for files, volumes, and virtual tapes in AWS. The service includes a highly-optimized data transfer mechanism, with bandwidth management, automated network resilience, and efficient data transfer, along with a local cache for low-latency on-premises access to your most active data. 

Return to [AWS services](amazon-web-services-cloud-platform.md).