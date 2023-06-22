---
sidebar_position: 2
---


# Configure Archiving and Restoring


![Archive settings](https://dytvr9ot2sszz.cloudfront.net/logz-docs/archive-and-restore/azure-aws-archive.png)

You can archive logs to either an Amazon S3 bucket or a Microsoft Azure Storage container.

The Logz.io archiver copies all incoming logs to your selected storage container. The data is archived in its "raw" state ~ pre-indexing and pre-mapping.

:::caution Important
Each account (or sub-account) should have its own archive configuration.
:::



**Related information**

You may also be interested in the API methods included in [**Archive logs**](https://docs.logz.io/api/#tag/Archive-logs) and [**Connect to AWS S3 Buckets**](https://docs.logz.io/api/#tag/Connect-to-S3-Buckets).

## Set up Archive and restore in AWS



**Before you begin, you'll need**:

* An AWS S3 bucket with appropriate permissions. The recommended permissions are `PutObject`, `ListBucket`, and `GetObject`. [Learn how to set up your **S3 permissions**](/user-guide/archive-and-restore/set-s3-permissions.html).
* The `logzio-verified` file in your bucket. This file is generated by Logz.io when you enable archiving in your account and is **required as part of the Logz.io authentication process**.

### 1. Enter your bucket information and S3 credentials

Select an authentication method. You can choose to authenticate with an IAM role
or an access key.

For stronger security,
we recommend authenticating with an IAM role.


* To set up an IAM role, see
  [_Give AWS access with IAM roles_]({{site.baseurl}}/user-guide/give-aws-access-with-iam-roles/).
* To set up an access key, see
  [_Give AWS access with access keys_]({{site.baseurl}}/user-guide/give-aws-access-with-access-keys/).

:::caution Important
Select a path to the **root of an S3 bucket**, to support data restore options. Data cannot be restored from a sub-bucket path.
:::

### 2. Test your connection and save

Click **Test connection** to make sure your bucket name and credentials
are valid and have the right permissions.

If everything checks out, click **Start archiving** to save your settings.
From now on, Logz.io will archive your logs as they come in.
You can stop archiving at any time.

### 3. Switching between IAM roles and Access keys

If you need to change your S3 configuration —
including switching between access key and IAM role authentication —
make the changes in the _Settings_ tab and click **Update settings**.

You can remove your credentials from Logz.io at any time
by clicking **Pause archiving**
and selecting **Remove my S3 settings** in the confirmation box.



## Set up Archive and restore in Microsoft Azure


**Before you begin, you'll need**:

* A Storage container with an App registration with appropriate permissions. [Learn more](/user-guide/archive-and-restore/azure-blob-permissions/#minimal-permissions).


### 1. Enter your container information and credentials

Fill in the form with the requested container information and IDs. [Detailed instructions](/user-guide/archive-and-restore/azure-blob-permissions/).

### 2. Test your connection and save

Click **Test connection** to make sure Logz.io can connect to your container and has the right permissions.

If everything checks out, click **Start archiving** to save your settings.
From now on, Logz.io will archive your logs as they come in.
You can stop archiving at any time.



## Restore archived logs


Restoring your archived logs will re-ingest them into a temporary account. You can search and navigate the restored account directly from your Logs account.

Restoring archived logs lets you view data in its original detail, allowing you to investigate events that are older than your plan's retention period.

[Learn more about how to manage your restored accounts.](https://docs.logz.io/user-guide/archive-and-restore/restore-archived-logs.html)

