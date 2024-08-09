# <code>_vpc()</code>
The base client for all constellation_vpc clients. Acts as a wrapper for the AWS CLI
***
### <code>_vpc(<span style="color:cyan;">region_name:str</span>, <span style="color:orange;">aws_access_key:str=None</span>, <span style="color:orange;">aws_access_secret_key:str=None</span>, <span style="color:yellow;">aws_sts_session_token:str=None</span>)</code>
- <code><span style="color:cyan;">region_name</span></code>
  - The region the client is configured to send requests to
- <code><span style="color:orange;">aws_access_key</span></code>
  - Provides the client with an AWS Access Key to use for authentication
- <code><span style="color:orange;">aws_access_secret_key</span></code>
  - Provides the AWS Secret Access Key for AWS Access Key Authentication 
- <code><span style="color:yellow;">aws_sts_session_token</span></code>
  - Provides the client with a session token from STS to use for authentication