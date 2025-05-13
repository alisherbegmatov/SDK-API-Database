# SDK-API-Database

- `/data/`: Contains all database-related files that store information about SDKs and APIs.
  - `sdk_api_list.json`: A JSON file containing a list of all SDKs and APIs with key details.
  - `sdk_api_versions.csv`: A CSV file containing versioning information for each SDK/API.
  - `sdk_api_metadata.csv`: A CSV file with additional metadata for each SDK/API, such as supported platforms, licensing, etc.
- `/docs/`: Documentation files related to the project.
  - `API_Usage_Guide.md`: A guide on how to use specific APIs and SDKs.
- `/scripts/`: Python scripts for processing or synchronizing the database files.

  - `generate_report.py`: Script to generate a report on the current state of SDKs/APIs in the database.
  - `sync_data.py`: Script for updating or syncing the database with new versions or SDKs/APIs.

- `README.md`: This file.

## Database Schema

The database contains the following primary fields for each entry:

1. **Name**:
   - Type: String
   - Description: The name of the SDK or API.
2. **Purpose**:
   - Type: String
   - Description: A short description of what the SDK or API does.
3. **Version**:
   - Type: String
   - Description: The version number of the SDK/API. This can help developers identify whether they are using the latest stable version or an outdated one.
4. **Business Entity**:

   - Type: String
   - Description: The organization or company responsible for maintaining the SDK/API.

5. **Documentation**:

   - Type: String
   - Description: A URL or reference to the official documentation, including setup guides and API reference.

6. **Integration Details**:
   - Type: String
   - Description: A brief guide or notes on how to integrate and use the SDK/API effectively.
7. **Supported Platforms**:

   - Type: String (optional)
   - Description: Platforms (e.g., iOS, Android, Web) where the SDK/API can be used.

8. **Licensing**:
   - Type: String (optional)
   - Description: Licensing information related to the SDK/API, e.g., MIT, GPL, proprietary.

## Example Entries

Below are some real SDKs and APIs that are included in this database:

### 1. **Stripe API**

- **Name**: Stripe API
- **Purpose**: Provides payment processing services for online stores and businesses.
- **Version**: v3.0.0
- **Business Entity**: Stripe, Inc.
- **Documentation**: [Stripe API Documentation](https://stripe.com/docs/api)
- **Integration Details**: To integrate Stripe, use their official SDK and follow the setup guide linked above.
- **Supported Platforms**: Web, iOS, Android
- **License**: Commercial

### 2. **Twilio API**

- **Name**: Twilio API
- **Purpose**: Cloud communications platform for sending and receiving text messages, voice calls, and video chats.
- **Version**: v4.5.0
- **Business Entity**: Twilio, Inc.
- **Documentation**: [Twilio API Documentation](https://www.twilio.com/docs/usage/api)
- **Integration Details**: Twilio provides SDKs for multiple programming languages and platforms. Follow their integration guides to set up messaging, calls, and more.
- **Supported Platforms**: Web, iOS, Android
- **License**: Commercial

### 3. **Firebase SDK**

- **Name**: Firebase SDK
- **Purpose**: Backend-as-a-Service (BaaS) platform to help developers build web and mobile apps faster. Offers features like authentication, real-time databases, analytics, and more.
- **Version**: v9.6.0
- **Business Entity**: Google
- **Documentation**: [Firebase Documentation](https://firebase.google.com/docs)
- **Integration Details**: Firebase SDK integrates with your mobile or web app using the provided SDK packages for authentication, databases, analytics, etc.
- **Supported Platforms**: Web, iOS, Android
- **License**: Commercial (Free Tier available)

### 4. **Google Maps API**

- **Name**: Google Maps API
- **Purpose**: Provides mapping services, geolocation, and location-based data for applications.
- **Version**: v3.44
- **Business Entity**: Google LLC
- **Documentation**: [Google Maps API Documentation](https://developers.google.com/maps/documentation)
- **Integration Details**: Add maps, geolocation, and places features to web and mobile apps by including the Google Maps JavaScript API or SDK.
- **Supported Platforms**: Web, iOS, Android
- **License**: Commercial

### 5. **Slack API**

- **Name**: Slack API
- **Purpose**: Enables integration of Slack messaging and collaboration platform with other applications.
- **Version**: v2.0.0
- **Business Entity**: Slack Technologies
- **Documentation**: [Slack API Documentation](https://api.slack.com/)
- **Integration Details**: Slack provides webhooks and SDKs to connect to messaging features, send notifications, and create custom integrations with third-party apps.
- **Supported Platforms**: Web, iOS, Android
- **License**: Commercial

### 6. **SendGrid API**

- **Name**: SendGrid API
- **Purpose**: Email delivery service that provides APIs to send transactional and marketing emails.
- **Version**: v7.5.0
- **Business Entity**: Twilio, Inc.
- **Documentation**: [SendGrid API Documentation](https://docs.sendgrid.com/)
- **Integration Details**: Use SendGrid’s API to send email programmatically. Integrate it into your backend services for email communication.
- **Supported Platforms**: Web
- **License**: Commercial

## How to Use

You can browse the database to find SDKs or APIs relevant to your project by referring to the following:

### Option 1: Directly Browse the JSON File

You can view or edit the database by opening the `sdk_api_list.json` file. This file is a structured JSON document that contains detailed information about each SDK/API.

Example of a JSON entry:

```json
{
  "name": "Stripe API",
  "purpose": "Payment processing for e-commerce platforms",
  "version": "v3.0.0",
  "business_entity": "Stripe, Inc.",
  "documentation": "https://stripe.com/docs/api",
  "integration_details": "To integrate Stripe, use their official SDK and follow the setup guide linked above.",
  "supported_platforms": "Web, iOS, Android",
  "license": "Commercial"
}
```
