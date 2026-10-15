

# How IAM works
<a name="intro-structure"></a>

AWS Identity and Access Management provides the infrastructure necessary to control authentication and authorization for your AWS account. 

First, a human user or an application uses their sign-in credentials to authenticate with AWS. IAM matches the sign-in credentials to a principal (an IAM user, AWS STS federated user principal, IAM role, or application) trusted by the AWS account and authenticates the principal to access AWS. 

Next, IAM makes a request to grant the principal access to resources. IAM grants or denies access in response to an authorization request. For example, when you first sign in to the console and are on the console Home page, you aren't accessing a specific service. When you select a service, you send an authorization request to IAM for that service. IAM verifies that your identity is on the list of authorized users, determines what policies control the level of access granted, and evaluates any other policies that might be in effect. Principals within your AWS account or from another AWS account that you trust can make authorization requests.

Once authorized, the principal can perform actions or operations on resources in your AWS account. For example, the principal could launch a new Amazon Elastic Compute Cloud instance, modify IAM group membership, or delete Amazon Simple Storage Service buckets. The following diagram illustrates this process through the IAM infrastructure:

![This diagram that shows how a principal is authenticated and authorized by the IAM service to perform actions or operations upon other AWS services or resources.](https://docs.aws.amazon.com/IAM/latest/UserGuide/images/intro-diagram _policies_800.png)


## Components of a request
<a name="intro-structure-request"></a>

When a principal tries to use the AWS Management Console, the AWS API, or the AWS CLI, that principal sends a *request* to AWS. The request includes the following information:
+ **Actions or operations** – The actions or operations that the principal wants to perform, such as an action in the AWS Management Console, or an operation in the AWS CLI or AWS API.
+ **Resources** – The AWS resource object upon which the principal requests to perform an action or operation.
+ **Principal** – The person or application that used an entity (user or role) to send the request. Information about the principal includes the permission policies. 
+ **Environment data** – Information about the IP address, user agent, SSL enabled status, and the timestamp.
+ **Resource data** – Data related to the resource requested, such as a DynamoDB table name or a tag on an Amazon EC2 instance.

AWS gathers the request information into a *request context*, which IAM evaluates to authorize the request.

## How principals are authenticated
<a name="intro-structure-authentication"></a>

A principal signs in to AWS using their credentials which IAM authenticates to permit the principal to send a request to AWS. Some services, such as Amazon S3 and AWS STS, allow specific requests from anonymous users. However, they're the exception to the rule. Each type of user goes through authentication.
+ **Root user** – Your sign in credentials used for authentication are the email address you used to create the AWS account and the password you specified at that time. 
+ **Federated principal** – Your identity provider authenticates you and passes your credentials to AWS, you don't have to sign-in directly to AWS. Both IAM Identity Center and IAM support identity federation.
+ **Users in AWS IAM Identity Center directory***(not federated)*– Users created directly in the IAM Identity Center default directory sign in using the AWS access portal and provide your username and password. 
+ **IAM user** – You sign-in by providing your account ID or alias, your username, and password. To authenticate workloads from the API or AWS CLI, you might use temporary credentials through assuming a role or you might use long-term credentials by providing your access key and secret key.

  To learn more about the IAM entities, see [IAM users](id_users.md) and [IAM roles](id_roles.md).

AWS recommends that you use multi-factor authentication (MFA) with all users to increase the security of your account. To learn more about MFA, see [AWS Multi-factor authentication in IAM](id_credentials_mfa.md). 

## Authorization and permission policy basics
<a name="intro-structure-authorization"></a>

Authorization refers to the principal having the required permissions to complete their request. During authorization, IAM identifies the policies that apply to the request using values from the request context. It then uses the policies to determine whether to allow or deny the request. IAM stores most permission policies as [JSON documents](access_policies.md#access_policies-json) that specify the permissions for principal entities. 

There are [several types of policies](access_policies.md) that can affect an authorization request. To provide your users with permissions to access the AWS resources in your account, you can use identity-based policies. Resource-based policies can grant [cross-account access](access_permissions-required.md#UserPermissionsAcrossAccounts). To make a request in a different account, a policy in the other account must allow you to access the resource *and* the IAM entity that you use to make the request must have an identity-based policy that allows the request.

IAM checks each policy that applies to the context of your request. IAM policy evaluation uses an *explicit deny*, which means that if a single permissions policy includes a denied action, IAM denies the entire request and stops evaluating. Because requests are *denied by default*, the applicable permissions policies must allow every part of your request for IAM to authorize your request. The evaluation logic for a request within a single account follows these basic rules:
+ By default, all requests are denied. (In general, requests made using the AWS account root user credentials for resources in the account are always allowed.) 
+ An explicit allow in any permissions policy (identity-based or resource-based) overrides this default.
+ The existence of an AWS Organizations service control policy (SCP) or resource control policy (RCP), IAM permissions boundary, or a session policy overrides the allow. If one or more of these policy types exists, they must all allow the request. Otherwise, it's implicitly denied. For more information on SCPs and RCPs, see [Authorization policies in AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_authorization_policies.html) in the *AWS Organizations User Guide*.
+ An explicit deny in any policy overrides any allows in any policy.

To learn more, see [Policy evaluation logic](reference_policies_evaluation-logic.md). <a name="intro-structure-actions"></a>

After IAM authenticates and authorizes the principal, IAM approves the actions or operations in their request by evaluating the permission policy that applies to the principal. Each AWS service defines the actions (operations) they support, and include things that you can do to a resource, such as viewing, creating, editing, and deleting that resource. The permission policy that applies to the principal must include the necessary actions to perform an operation. To learn more about how IAM evaluates permission policies, see [Policy evaluation logic](reference_policies_evaluation-logic.md).

The service defines a set of actions that a principal can perform on each resource. When creating permission policies, make sure to include the actions that you want the user to be able to perform. For example, IAM supports over 40 actions for a user resource, including the following basic actions:
+ `CreateUser`
+ `DeleteUser`
+ `GetUser`
+ `UpdateUser`

In addition, you can specify conditions in your permission policy that provide access to resources when the request meets the specified conditions. For example, you might want a policy statement to take effect after a specific date or to control access when a specific value appears in an API. To specify conditions, you use the [`Condition`](reference_policies_elements_condition_operators.md) element of a policy statement. 

After IAM approves the operations in a request, the principal can work with the related resources in your account. A resource is an object that exists within a service. Examples include an Amazon EC2 instance, an IAM user, and an Amazon S3 bucket. If the principal creates a request to perform an action on a resource that isn't included in the permission policy, the service denies the request. For example, if you have permission to delete an IAM role but request to delete an IAM group, the request fails if you don't have permission to delete IAM groups. To learn more about which actions, resources, and condition keys the different AWS services support, see [Actions, Resources, and Condition Keys for AWS Services](https://docs.aws.amazon.com/reference_policies_actions-resources-contextkeys.html).