Google App Engine - OAuth Profile
=================================

This Google App Engine application provides a OAuth and Web Service Endpoint to
access the specific Google Account information provided to Google App Engine.

The following example shows a dictionary of returned information:

    {
      "id": "123456789123456789123"
      "email": "example@googlemail.com",
      "nickname": "example"
    }

OAuth Endpoint
--------------
- Getting a Request Token:
  https://oauth-profile.appspot.com/_ah/OAuthGetRequestToken
- Redirecting a User to Authorize:
  https://oauth-profile.appspot.com/_ah/OAuthAuthorizeToken
- Getting an Access Token:
  https://oauth-profile.appspot.com/_ah/OAuthGetAccessToken

Web Service Endpoint
--------------------
- Retrieving the User Information:
  https://oauth-profile.appspot.com/oauth/v1/userinfo

Documentation
-------------
- OAuth for Python Overview:
  https://developers.google.com/appengine/docs/python/oauth/overview
- Registration for Web-Based Applications:
  https://developers.google.com/accounts/docs/RegistrationForWebAppsAuto

License
-------
* Released under MIT License
* Copyright (c) 2012 Marc Hoersken <info@marc-hoersken.de>
