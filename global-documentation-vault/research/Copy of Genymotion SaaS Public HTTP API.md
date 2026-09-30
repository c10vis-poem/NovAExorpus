# Copy of Genymotion SaaS Public HTTP API

Genymotion SaaS Public HTTP API (2.0.0)
Download OpenAPI specification:
Download
Genymotion SaaS Team: genymotion-cloud@genymobile.com
URL: https://cloud.geny.io/
Genymotion SaaS user documentation can be found at docs.genymotion.com/saas.
This HTTP API allows you to manage Genymotion SaaS virtual devices.
There are 3 main concepts in this API. All of them must be understood in order to able to use
the it efficiently.
The first concept is Authentication. An API token or JWT (JSON Web Token) must be used to
authenticate the API calls. The authentication endpoint itself does not accept an API token or
JWT. In the Genymotion SaaS Public HTTP API, all endpoints other than the authentication
endpoint accept either API token or JWT authentication.
For endpoints requiring authentication, exactly one of the API token or the JWT must be
provided. If neither are provided, the API call will return a 401 Unauthorized HTTP error. If
both are provided, the API call will return a 400 Bad Request HTTP error.
The details of each authentication scheme are provided below, in Authentication.
The second concept is the Recipe. A Recipe is what is needed to cook an Instance. This
Recipe contains the information about the Android system, the virtual device characteristics,
and some contextual data. Genymobile provides a variety of default Recipes, but you can
create and share new ones from either the Genymotion SaaS Portal or from the Genymotion
Desktop software (license required).
The third concept is the Instance. An Instance represents a Genymotion Virtual Device
running in the Cloud. Built using the information contained in a Recipe, an Instance can be
accessed using a wide variety of tools. The current API allows you to start and stop
disposable Instances. A disposable Instance will always be recreated from the Recipe when a
start request is sent. When a stop request is sent, the virtual device Instance will be
destroyed, and any modifications done inside it during the run time will be lost.
Users v1
|
Authenticate User


Authenticate a User, and retreive a new valid JWT. This JWT must be provided to all other API
calls in order to identify and authenticate the User executing the request.
Once logged in, simply add the Authorization HTTP header to all subsequents API calls.
Authorization HTTP header value must have the following format: Bearer <JWT> .
A JWT will expire after some time. The default validity duration is 48 hours. It is
recommended to generate a new one before running a new set of API calls. Generating a new
JWT will not invalidate previously generated JWTs.
REQUEST BODY SCHEMA: application/json
required
Data used to log User
string <email> (Email)
Email address
string <password>
User password
Responses
200
User profile and JWT
401
The email/password combination is incorrect.
403
User is not enabled.
default
Cannot log in user.
Request samples
email
required
password
required
POST
/v1/users/login


Recipes v1
Payload
Shell
Python
Response samples
200
401
403
default
application/json
Copy
{
"email": "user@example.com",
"password": "pa$$word"
}
application/json
Expand all
Collapse all
Copy
{
"token": "string",
"user": 
-
{
"created_at": 0,
"email": "user@example.com",
"first_name": "string",
"is_enabled": true,
"is_organization_manager": true,
"is_validated": true,
"last_name": "string",
"role": "USER",
"uuid": "095be615-a8ad-4c33-8e9c-c7612fbf6c9f",
"groups":  … 
+
[
],
"front_preferences": { },
"tnc_accepted": true,
"organization":  … 
+
{
},
"group":  … 
+
{
}
}
}
Content type
Content type


List Recipes (deprecated) Deprecated
This route is deprecated and will be removed in a future release.
To avoid any service disruption, it is mandatory to migrate your calls to the new List Recipe
v3 route.
List all ready Recipes available for the authenticated User. This endpoint returns 3 lists of
Recipes:
Bases Recipes, the default Recipes, provided by Genymobile and always available to all
Users
User Recipes, Recipes shared to any other User by the currently authenticated User
Shared Recipes, Recipes shared by any other User to the currently authenticated User
AUTHORIZATIONS:
ApiToken or Bearer
Responses
200
List of Recipes
default
Cannot list recipes.
Request samples
Shell
Python
curl -H 'Content-Type: application/json;charset=utf-8' -H 'x-api-token: <token>
Response samples
GET
/v1/recipes
Copy


200
default
application/json
Expand all
Collapse all
Copy
{
"base": 
-
[
 … 
+ {
}
],
"user": 
-
[
 … 
+ {
}
],
"shared": 
-
[
 … 
+ {
}
]
}
Create a new recipe
This endpoint creates a new recipe from the input parameters.
AUTHORIZATIONS:
ApiToken or Bearer
REQUEST BODY SCHEMA: application/json
required
string <uuid> (Uuidv4) ^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][...
Show pattern
Resource unique identifier
string <uuid> (Uuidv4) ^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][...
Show pattern
Resource unique identifier
string or null <uuid> (NullableUuidv4) ^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][...
Show pattern
Resource unique identifier
string or null
Recipe name
string
Recipe description
hardware_profile_uuid
required
os_image_uuid
required
parent_recipe_uuid
name
required
description
Content type


Responses
201
The created recipe.
400
Wrong parameters.
401
Not authorized.
403
Not allowed.
500
Service Failed.
Request samples
Payload
Shell
Python
Response samples
201
400
401
403
500
POST
/v1/recipes
application/json
Copy
{
"hardware_profile_uuid": "45d3646a-9489-4a40-aa87-addaa499c31b",
"os_image_uuid": "d46548f5-0f78-43d8-b745-5f67ed0c7915",
"parent_recipe_uuid": "7f02aa13-3f42-4289-88bd-199e2080217c",
"name": "string",
"description": "string"
}
Content type


application/json
Expand all
Collapse all
Copy
{
"parent_recipe_uuid": "7f02aa13-3f42-4289-88bd-199e2080217c",
"uuid": "095be615-a8ad-4c33-8e9c-c7612fbf6c9f",
"hardware_profile": 
-
{
"uuid": "095be615-a8ad-4c33-8e9c-c7612fbf6c9f",
"name": "string",
"form_factor": "PHONE",
"is_official": true,
"recipe_count": 0
},
"os_image": 
-
{
"uuid": "095be615-a8ad-4c33-8e9c-c7612fbf6c9f",
"name": "string",
"is_official": true,
"recipe_count": 0
},
"name": "string",
"is_official": true,
"owner": 
-
{
"created_at": 0,
"email": "user@example.com",
"first_name": "string",
"is_enabled": true,
"is_organization_manager": true,
"is_validated": true,
"last_name": "string",
"role": "USER",
"uuid": "095be615-a8ad-4c33-8e9c-c7612fbf6c9f",
"groups":  … 
+
[
],
"organization":  … 
+
{
}
},
"description": "string",
"created_at": "string",
"updated_at": "string",
"status": "CREATING"
}
Delete Recipe identified by its uuid
AUTHORIZATIONS:
ApiToken or Bearer
PATH PARAMETERS
string <uuid> ^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][...
Show pattern
Uuid of the recipe to retrieve
uuid
required
Content type


REQUEST BODY SCHEMA: application/json
boolean
Default: false
Define if we delete the recipe hardware profile.
boolean
Default: false
Define if we delete the recipe OS image.
Responses
— 204
Recipe is successfully removed.
400
Wrong parameters.
401
Not authorized.
403
The user is not allowed to delete this recipe.
404
Recipe not found.
500
Service Failed.
Request samples
Payload
Shell
Python
delete_hardware_profile
delete_os_image
DELETE
/v1/recipes/{uuid}


Recipes v2
Response samples
400
401
403
404
500
application/json
Copy
{
"delete_hardware_profile": false,
"delete_os_image": false
}
application/json
Copy
{
"code": "string",
"message": "string"
}
List Recipes (paginated) (deprecated) Deprecated
This route is deprecated and will be removed in a future release.
To avoid any service disruption, it is mandatory to migrate your calls to the new List Recipe
v3 route.
List all Recipes available for the authenticated User.
This endpoint returns a paginated list of all Recipes.
AUTHORIZATIONS:
ApiToken or Bearer
QUERY PARAMETERS
Content type
Content type


string
Default: "all"
Enum: "all"
"official"
"owner"
"sharee"
"shared"
Filter by Recipe source.
Options are:
official : Recipes provided by Genymotion, available to
everyone
owner : Recipes created by authenticated User
sharee : Recipes shared to authenticated User or their
Organization
shared : combination of owner & sharee
all : combination of official & shared
string
Default: "all"
Enum: "all"
"ready"
"updating"
Filter by Recipe status.
Options are:
ready : Recipes you can use to start an Instance with
updating : Recipes currently being updating (cannot be used to
start an Instance yet)
all : combination of ready & updating
string
Default: "system"
Enum: "system"
"app"
"all"
Filter by Recipe type.
Options are:
system : Recipes based on a full-fledged system
app : Recipes based on an Android application (APK)
all : combination of system & app
Responses
200
Paginated list of Recipes
source
status
type


Recipes v3
default
Cannot list recipes.
Request samples
Shell
Python
curl -H 'Content-Type: application/json;charset=utf-8' -H 'x-api-token: <token>
Response samples
200
default
GET
/v2/recipes
Copy
application/json
Expand all
Collapse all
Copy
{
"count": 0,
"next": "string",
"previous": "string",
"results": 
-
[
 … 
+ {
}
]
}
List Recipes
Content type


List all is official Recipes and Recipes of the current user.
AUTHORIZATIONS:
ApiToken or Bearer
QUERY PARAMETERS
string
Default: "all"
Enum: "all"
"official"
"shared"
Filter by Recipe source. Options are:
official : Recipes provided by Genymotion, available to
everyone
shared : combination of recipes :
created by the authenticated User
shared to authenticated User or their Organization
all : combination of official & shared
Array of strings
Default: "x86_64,x86"
Items Enum: "x86"
"x86_64"
"arm64"
Filter by the architecture of the related image.
If this isn't specified, x86 and x86_64 will be used by default.
string
Search term to search on name or uuid attributes.
integer
Page to fetch
integer
Default: 30
Number of recipes per page
Responses
200
A list containing all official and related to the user recipes.
401
Not authorized.
source
arch
search
page
page_size


Instances v1
500
Service Failed.
Request samples
Shell
Python
curl -H 'Content-Type: application/json;charset=utf-8' -H 'x-api-token: <token>
Response samples
200
401
500
GET
/v3/recipes/
Copy
application/json
Expand all
Collapse all
Copy
{
"count": 0,
"results": 
-
[
 … 
+ {
}
]
}
Start disposable Instance
Start a new disposable Instance from the given Recipe identified by its Uuid.
Content type


The Instance is disposable, meaning that all changes done inside it will be lost after the
Instance is stopped.
The state of the Instance returned by this call will always be CREATING.
AUTHORIZATIONS:
ApiToken or Bearer
PATH PARAMETERS
string <uuid> ^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][...
Show pattern
Uuid of the resource
REQUEST BODY SCHEMA: application/json
required
Data used to start new disposable Instance
string
Name of the Instance. This name must be unique per User.
boolean
Default: false
In case a virtual device already exist with the same name, allow the
Platform to rename the Instance with a new, unique, name. New
name will look like instance_name followed by some characters
generated by the Platform.
boolean
Default: false
DEPRECATED. Use timeouts.inactivity instead.
object
DEPRECATED. Use timeouts instead.
object
Various customizable timeouts for the Instance.
Responses
201
The creating Instance
400
An instance with the same name already exist for user.
uuid
required
instance_name
required
rename_on_conflict
stop_when_inactive
automatic_release
timeouts


403
Not allowed to start an instance.
404
The given recipe cannot be found, or no slots are available on the platform.
default
Cannot start disposable instance.
Request samples
Payload
Shell
Python
Response samples
201
400
403
404
default
POST
/v1/recipes/{uuid}/start-disposable
application/json
Expand all
Collapse all
Copy
{
"instance_name": "string",
"rename_on_conflict": false,
"stop_when_inactive": false,
"automatic_release": 
-
{
"type": "none"
},
"timeouts": { }
}
application/json
Expand all
Collapse all
Copy
{
"uuid": "095be615-a8ad-4c33-8e9c-c7612fbf6c9f",
"name": "string",
"owner_uuid": "a528e82a-c54a-4046-8831-44d7f9028f54",
"organization_uuid": "5d67373d-71ba-435a-bb8a-e71f4d7e2958",
Content type
Content type


"hardware_profile": 
-
{
"uuid": "095be615-a8ad-4c33-8e9c-c7612fbf6c9f",
"owner":  … 
+
{
},
"name": "string",
"is_official": true,
"form_factor": "string",
"cpu_count": 0,
"ram_size": 0,
"data_disk_size": 0,
"width": 0,
"height": 0,
"density": 0,
"hw_navigation_keys": true
},
"os_image": 
-
{
"uuid": "095be615-a8ad-4c33-8e9c-c7612fbf6c9f",
"owner":  … 
+
{
},
"name": "string",
"is_official": true,
"image_version": "string",
"arch": "x86",
"is_beta": true,
"build_date": "string",
"os_version":  … 
+
{
}
},
"state": "CREATING",
"streamer_fqdn": "string",
"turn_fqdn": "string",
"adb_url": "string",
"file_upload_url": "string",
"webrtc_url": "string",
"recipe_uuid": "597eb633-0943-4de5-b80a-1b0319522204",
"created_at": "string",
"updated_at": "string",
"timeout": 0,
"timeouts": 
-
{
"global": 0,
"inactivity": 0
},
"recipe": 
-
{
"uuid": "095be615-a8ad-4c33-8e9c-c7612fbf6c9f",
"name": "string",
"source": "genymotion",
"owner_uuid": "a528e82a-c54a-4046-8831-44d7f9028f54",
"status": "ready",
"items":  … 
+
[
],
"created_at": "string",
"updated_at": "string",
"owner":  … 
+
{
},
"is_official": true
},


"owner": 
-
{
"created_at": 0,
"email": "user@example.com",
"first_name": "string",
"is_enabled": true,
"is_organization_manager": true,
"is_validated": true,
"last_name": "string",
"role": "USER",
"uuid": "095be615-a8ad-4c33-8e9c-c7612fbf6c9f",
"groups":  … 
+
[
],
"organization":  … 
+
{
},
"group":  … 
+
{
}
}
}
List Instances (deprecated) Deprecated
This route is deprecated and will be removed in a future release.
To avoid any service disruption, it is mandatory to migrate your calls to the new List
Instances v2 route.
List all currently available Instances for the authenticated User. This endpoint is deprecated.
/v2/instances should be used instead.
AUTHORIZATIONS:
ApiToken or Bearer
QUERY PARAMETERS
string
Enum: "template"
"recipe"
Deprecated.
Responses
200
List of Instances
format


default
Cannot list instances.
Request samples
Shell
Python
curl -H 'Content-Type: application/json;charset=utf-8' -H 'x-api-token: <token>
Response samples
200
default
GET
/v1/instances
Copy
application/json
Expand all
Collapse all
Copy
[
- {
"uuid": "095be615-a8ad-4c33-8e9c-c7612fbf6c9f",
"name": "string",
"owner_uuid": "a528e82a-c54a-4046-8831-44d7f9028f54",
"organization_uuid": "5d67373d-71ba-435a-bb8a-e71f4d7e2958",
"hardware_profile":  … 
+
{
},
"os_image":  … 
+
{
},
"state": "CREATING",
"streamer_fqdn": "string",
"turn_fqdn": "string",
"adb_url": "string",
"file_upload_url": "string",
"webrtc_url": "string",
"recipe_uuid": "597eb633-0943-4de5-b80a-1b0319522204",
"created_at": "string",
"updated_at": "string",
"timeout": 0,
"timeouts":  … 
+
{
}
}
]
Content type


Get a token to connect to an instance.
Returns a token to be used for connecting to an instance.
AUTHORIZATIONS:
ApiToken or Bearer
REQUEST BODY SCHEMA: application/json
string <uuid>
Instance uuid.
This is required to connect to instances with arm64 architecture.
Responses
200
Instance access token
default
An unknown error occurred
Request samples
Payload
instance_uuid
POST
/v1/instances/access-token
application/json
Copy
{
"instance_uuid": "7e61f2db-030b-4d58-8326-9509e91716e2"
}
Content type


Response samples
200
default
application/json
Copy
{
"access_token": "string"
}
Get Instance
Retrieve an Instance identified by its Uuid.
AUTHORIZATIONS:
ApiToken or Bearer
PATH PARAMETERS
string <uuid> ^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][...
Show pattern
Uuid of the resource
QUERY PARAMETERS
string
Default: "recipe"
Enum: "recipe"
"template"
Deprecated.
Responses
200
The Instance
404
Instance does not exit.
uuid
required
format
Content type


default
Cannot get instance information.
Request samples
Shell
Python
curl -H 'Content-Type: application/json;charset=utf-8' -H 'x-api-token: <token>
Response samples
200
404
default
GET
/v1/instances/{uuid}
Copy
application/json
Expand all
Collapse all
Copy
{
"uuid": "095be615-a8ad-4c33-8e9c-c7612fbf6c9f",
"name": "string",
"owner_uuid": "a528e82a-c54a-4046-8831-44d7f9028f54",
"organization_uuid": "5d67373d-71ba-435a-bb8a-e71f4d7e2958",
"hardware_profile": 
-
{
"uuid": "095be615-a8ad-4c33-8e9c-c7612fbf6c9f",
"owner":  … 
+
{
},
"name": "string",
"is_official": true,
"form_factor": "string",
"cpu_count": 0,
"ram_size": 0,
"data_disk_size": 0,
"width": 0,
"height": 0,
"density": 0,
"hw_navigation_keys": true
},
Content type


"os_image": 
-
{
"uuid": "095be615-a8ad-4c33-8e9c-c7612fbf6c9f",
"owner":  … 
+
{
},
"name": "string",
"is_official": true,
"image_version": "string",
"arch": "x86",
"is_beta": true,
"build_date": "string",
"os_version":  … 
+
{
}
},
"state": "CREATING",
"streamer_fqdn": "string",
"turn_fqdn": "string",
"adb_url": "string",
"file_upload_url": "string",
"webrtc_url": "string",
"recipe_uuid": "597eb633-0943-4de5-b80a-1b0319522204",
"created_at": "string",
"updated_at": "string",
"timeout": 0,
"timeouts": 
-
{
"global": 0,
"inactivity": 0
},
"recipe": 
-
{
"uuid": "095be615-a8ad-4c33-8e9c-c7612fbf6c9f",
"name": "string",
"source": "genymotion",
"owner_uuid": "a528e82a-c54a-4046-8831-44d7f9028f54",
"status": "ready",
"items":  … 
+
[
],
"created_at": "string",
"updated_at": "string",
"owner":  … 
+
{
},
"is_official": true
},
"owner": 
-
{
"created_at": 0,
"email": "user@example.com",
"first_name": "string",
"is_enabled": true,
"is_organization_manager": true,
"is_validated": true,
"last_name": "string",
"role": "USER",
"uuid": "095be615-a8ad-4c33-8e9c-c7612fbf6c9f",
"groups":  … 
+
[
],
"organization":  … 
+
{
},
"group":  … 
+
{
}
}
}
Stop disposable Instance


Stop the given disposable Instance identified by its Uuid.
The Instance will automatically be destroyed right after it has been stopped.
The state of the Instance returned by this call will always be STOPPING, unless it was already
in SAVING or DELETING state. In this case, the call will succeed but the instance will continue
its end-of-life cycle.
AUTHORIZATIONS:
ApiToken or Bearer
PATH PARAMETERS
string <uuid> ^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][...
Show pattern
Uuid of the resource
Responses
200
The stopping Instance
404
Instance does not exit
default
Cannot stop disposable instance.
Request samples
Shell
Python
import requests
requests post 'https://api.geny.io/cloud/v1/instances/<UUID>/stop-disposable' 
uuid
required
POST
/v1/instances/{uuid}/stop-disposable
Copy
.
(
,


   'x-api-token' '<token>'
Response samples
200
404
default
:
})
application/json
Expand all
Collapse all
Copy
{
"uuid": "095be615-a8ad-4c33-8e9c-c7612fbf6c9f",
"name": "string",
"owner_uuid": "a528e82a-c54a-4046-8831-44d7f9028f54",
"organization_uuid": "5d67373d-71ba-435a-bb8a-e71f4d7e2958",
"hardware_profile": 
-
{
"uuid": "095be615-a8ad-4c33-8e9c-c7612fbf6c9f",
"owner":  … 
+
{
},
"name": "string",
"is_official": true,
"form_factor": "string",
"cpu_count": 0,
"ram_size": 0,
"data_disk_size": 0,
"width": 0,
"height": 0,
"density": 0,
"hw_navigation_keys": true
},
"os_image": 
-
{
"uuid": "095be615-a8ad-4c33-8e9c-c7612fbf6c9f",
"owner":  … 
+
{
},
"name": "string",
"is_official": true,
"image_version": "string",
"arch": "x86",
"is_beta": true,
"build_date": "string",
"os_version":  … 
+
{
}
},
"state": "CREATING",
"streamer_fqdn": "string",
"turn_fqdn": "string",
"adb_url": "string",
"file_upload_url": "string",
"webrtc_url": "string",
"recipe_uuid": "597eb633-0943-4de5-b80a-1b0319522204",
"created_at": "string",
"updated_at": "string",
"timeout": 0,
"timeouts": 
-
{
"global": 0,
"inactivity": 0
},
Content type


"recipe": 
-
{
"uuid": "095be615-a8ad-4c33-8e9c-c7612fbf6c9f",
"name": "string",
"source": "genymotion",
"owner_uuid": "a528e82a-c54a-4046-8831-44d7f9028f54",
"status": "ready",
"items":  … 
+
[
],
"created_at": "string",
"updated_at": "string",
"owner":  … 
+
{
},
"is_official": true
},
"owner": 
-
{
"created_at": 0,
"email": "user@example.com",
"first_name": "string",
"is_enabled": true,
"is_organization_manager": true,
"is_validated": true,
"last_name": "string",
"role": "USER",
"uuid": "095be615-a8ad-4c33-8e9c-c7612fbf6c9f",
"groups":  … 
+
[
],
"organization":  … 
+
{
},
"group":  … 
+
{
}
}
}
Save a running instance in order to reuse it later
[STATEFULL] Export running instance data to make it persist over stop
AUTHORIZATIONS:
ApiToken or Bearer
PATH PARAMETERS
string <uuid> ^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][...
Show pattern
UUID of the instance
REQUEST BODY SCHEMA: application/json
string
Default: "SAVE_AS"
Enum: "SAVE"
"SAVE_AS"
Specify if the recipe should be updated in place, or if a new recipe
should be created.
uuid
required
action


SAVE will update the custom recipe. SAVE can only be used if the
current user is the owner of the custom recipe. If a the image is
official, a new custom image will be created. Otherwise the existing
custom image will be updated.
SAVE_AS will create a new custom recipe and a new custom image.
When a new custom recipe is created, it will have the name specified
by new_recipe_name. If no new_recipe_name is specified, the new
custom recipe will be named "Copy of toriginal recipe name)"
When a new custom image is created, it will have the name specified
by new_os_image_name. If no new_os_image_name is specified, the
new custom image will be named "Copy of (original image name)"
string
Name of the new created recipe. Used in case of action=SAVE_AS.
string
Name of the new created OS Image. Used in case of action=SAVE and
current OsImage is official, or if action=SAVE_AS.
Responses
— 204
The instance has successfully been saved.
403
The user is not allowed to save an instance.
404
Instance not found.
500
Service Failed.
Request samples
new_recipe_name
new_os_image_name
POST
/v1/instances/{uuid}/save


Instances v2
Payload
Shell
Python
Response samples
403
404
500
application/json
Copy
{
"action": "SAVE",
"new_recipe_name": "string",
"new_os_image_name": "string"
}
application/json
Copy
{
"code": "string",
"message": "string"
}
List Instances
List all currently available Instances for the authenticated User.
The following sortable fields are available:
name (Instance name)
created_at (Instance creation datetime)
updated_at (Instance update datetime)
owner (Uuid of the Instance owner)
state (Instance state)
Content type
Content type


This endpoint is paginated.
AUTHORIZATIONS:
ApiToken or Bearer
QUERY PARAMETERS
string^[+-]?[0-9A-Za-z_-]*$
Use an orderable field with an optional '+' OR '-' prefix to order in the
desired direction
integer
Page to query
integer
Number of elements per pages
string <uuid> ^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][...
Show pattern
Uuid of the organization. Only an organization manager can use this
filter.
string
Instance state to filter
Responses
200
List of Instances
403
Not allowed to list organization's instances
default
Cannot list instances.
Request samples
ordering
page
page_size
organization_uuid
state
GET
/v2/instances


Hardware Profile v1
Shell
Python
curl -H 'Content-Type: application/json;charset=utf-8' -H 'x-api-token: <token>
Response samples
200
403
default
Copy
application/json
Expand all
Collapse all
Copy
{
"count": 0,
"next": "string",
"previous": "string",
"results": 
-
[
 … 
+ {
}
]
}
Retrieve Hardware Profile identified by its uuid
AUTHORIZATIONS:
ApiToken or Bearer
PATH PARAMETERS
string <uuid> ^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][...
Show pattern
Uuid of the hardware profile to retrieve
Responses
uuid
required
Content type


200
The requested hardware profile.
403
The user is not allowed to request this hardware profile.
404
Hardware Profile not found.
500
Service Failed.
Request samples
Shell
Python
curl -H 'Content-Type: application/json;charset=utf-8' -H 'x-api-token: <token>
Response samples
200
403
404
500
GET
/v1/hardware-profiles/{uuid}
Copy
application/json
Expand all
Collapse all
Copy
{
"uuid": "095be615-a8ad-4c33-8e9c-c7612fbf6c9f",
"display_settings": 
-
{
"uuid": "095be615-a8ad-4c33-8e9c-c7612fbf6c9f",
"displays":  … 
+
[
],
"display_mode": "REGULAR",
"hw_navigation_keys": true
},
"parent_hardware_profile_uuid": "c2b24ad9-266c-4839-915f-e2ff070fbe70",
"name": "string",
"is_official": true,
Content type


"owner": 
-
{
"created_at": 0,
"email": "user@example.com",
"first_name": "string",
"is_enabled": true,
"is_organization_manager": true,
"is_validated": true,
"last_name": "string",
"role": "USER",
"uuid": "095be615-a8ad-4c33-8e9c-c7612fbf6c9f",
"groups":  … 
+
[
],
"organization":  … 
+
{
}
},
"form_factor": "PHONE",
"cpu_count": 0,
"ram_size": 0,
"data_disk_size": 0,
"release_date": "string",
"created_at": "string",
"updated_at": "string",
"recipe_count": 0
}
Delete Hardware Profile identified by its uuid
AUTHORIZATIONS:
ApiToken or Bearer
PATH PARAMETERS
string <uuid> ^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][...
Show pattern
Uuid of the hardware profile to retrieve
Responses
— 204
Hardware Profile is successfully removed.
401
Not authorized.
403
The user is not allowed to delete this hardware profile.
uuid
required


404
Hardware Profile not found.
500
Service Failed.
Request samples
Shell
Python
curl -H 'Content-Type: application/json;charset=utf-8' -H 'x-api-token: <token>
Response samples
401
403
404
500
DELETE
/v1/hardware-profiles/{uuid}
Copy
application/json
Copy
{
"code": "string",
"message": "string"
}
List Hardware Profiles
List all is official Hardware Profiles and Hardware Profiles of the current user.
AUTHORIZATIONS:
ApiToken or Bearer
QUERY PARAMETERS
Content type


string
Default: "all"
Enum: "all"
"official"
"owner"
Filter by Hardware Profile source. Options are:
official : Hardware Profiles provided by Genymotion, available
to everyone
owner : Hardware Profiles created by authenticated User
all : combination of official & owner
string
Search term to search on name attribute.
integer
Page to fetch
integer
Default: 30
Number of hardware profiles per page
Responses
200
A list containing all official and related to the user hardware profiles.
401
Not authorized.
500
Service Failed.
Request samples
Shell
Python
source
search
page
page_size
GET
/v1/hardware-profiles/


curl -H 'Content-Type: application/json;charset=utf-8' -H 'x-api-token: <token>
Response samples
200
401
500
Copy
application/json
Expand all
Collapse all
Copy
{
"count": 0,
"results": 
-
[
 … 
+ {
}
]
}
Create a new hardware profile
This endpoint creates a new hardware profile from the input parameters.
AUTHORIZATIONS:
ApiToken or Bearer
REQUEST BODY SCHEMA: application/json
required
object (PublicDisplaySettingsPayload)
string or null <uuid> (NullableUuidv4) ^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]
{3}-[89ab][...
Show pattern
Resource unique identifier
string
Hardware Profile name
string (PublicFormFactor)
Enum: "PHONE"
"TABLET"
"AUTOMOTIVE"
Hardware Profile form factor
integer
display_settings
required
parent_hardware_profile_uuid
name
required
form_factor
cpu_count
Content type


Default: 4
Enum: 1
2
4
8
Hardware Profile Cpu count
integer
Default: 4096
Enum: 1024
2048
3072
4096
6144
8192
Hardware Profile RAM size in Mb
string or null (NullableShortDate) ^(\d{4})-(\d){2}-(\d{2})$
Date
Responses
201
The created hardware profile.
400
Wrong parameters.
401
Not authorized.
403
Not allowed.
500
Service Failed.
Request samples
Payload
Shell
Python
ram_size
release_date
POST
/v1/hardware-profiles/


Response samples
201
400
401
403
500
application/json
Expand all
Collapse all
Copy
{
"display_settings": 
-
{
"displays":  … 
+
[
],
"hw_navigation_keys": true
},
"parent_hardware_profile_uuid": "c2b24ad9-266c-4839-915f-e2ff070fbe70",
"name": "string",
"form_factor": "PHONE",
"cpu_count": 4,
"ram_size": 4096,
"release_date": "string"
}
application/json
Expand all
Collapse all
Copy
{
"uuid": "095be615-a8ad-4c33-8e9c-c7612fbf6c9f",
"display_settings": 
-
{
"uuid": "095be615-a8ad-4c33-8e9c-c7612fbf6c9f",
"displays":  … 
+
[
],
"display_mode": "REGULAR",
"hw_navigation_keys": true
},
"parent_hardware_profile_uuid": "c2b24ad9-266c-4839-915f-e2ff070fbe70",
"name": "string",
"is_official": true,
"owner": 
-
{
"created_at": 0,
"email": "user@example.com",
"first_name": "string",
"is_enabled": true,
"is_organization_manager": true,
"is_validated": true,
"last_name": "string",
"role": "USER",
"uuid": "095be615-a8ad-4c33-8e9c-c7612fbf6c9f",
"groups":  … 
+
[
],
"organization":  … 
+
{
}
},
"form_factor": "PHONE",
"cpu_count": 0,
"ram_size": 0,
"data_disk_size": 0,
"release_date": "string",
Content type
Content type


OS Image v1
"created_at": "string",
"updated_at": "string",
"recipe_count": 0
}
Retrieve OS Image identified by its uuid
AUTHORIZATIONS:
ApiToken or Bearer
PATH PARAMETERS
string <uuid> ^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][...
Show pattern
Uuid of the OS Image to retrieve
Responses
200
The requested OS Image.
403
The user is not allowed to request this OS Image.
404
OS Image not found.
500
Service Failed.
uuid
required


Request samples
Shell
Python
curl -H 'Content-Type: application/json;charset=utf-8' -H 'x-api-token: <token>
Response samples
200
403
404
500
GET
/v1/os-images/{uuid}
Copy
application/json
Expand all
Collapse all
Copy
{
"uuid": "095be615-a8ad-4c33-8e9c-c7612fbf6c9f",
"os_version": 
-
{
"uuid": "095be615-a8ad-4c33-8e9c-c7612fbf6c9f",
"name": "string",
"os_version": "string",
"sdk_version": "string",
"release_date": "string"
},
"parent_os_image_uuid": "cbcb716b-9ff1-4221-877f-79705bbb170e",
"supported_form_factors": 
-
[
"PHONE"
],
"name": "string",
"is_official": true,
"is_beta": true,
"arch": "x86",
"owner": 
-
{
"created_at": 0,
"email": "user@example.com",
"first_name": "string",
"is_enabled": true,
"is_organization_manager": true,
"is_validated": true,
"last_name": "string",
"role": "USER",
"uuid": "095be615-a8ad-4c33-8e9c-c7612fbf6c9f",
"groups":  … 
+
[
],
"organization":  … 
+
{
}
},
"status": "CREATING",
"image_version": "string",
"image_uri": "string",
Content type


"image_size_bytes": 0,
"image_hash": "string",
"image_date": "string",
"build_date": "string",
"created_at": "string",
"updated_at": "string",
"recipe_count": 0
}
Delete OS Image identified by its uuid
AUTHORIZATIONS:
ApiToken or Bearer
PATH PARAMETERS
string <uuid> ^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][...
Show pattern
Uuid of the OS Image to retrieve
Responses
— 204
OS Image is successfully removed.
400
Wrong parameters.
401
Not authorized.
403
The user is not allowed to delete this Os Image.
404
OS Image not found.
uuid
required


500
Service Failed.
Request samples
Shell
Python
curl -H 'Content-Type: application/json;charset=utf-8' -H 'x-api-token: <token>
Response samples
400
401
403
404
500
DELETE
/v1/os-images/{uuid}
Copy
application/json
Copy
{
"code": "string",
"message": "string"
}
List OS Images
List all is official OS Images and OS Images of the current user.
AUTHORIZATIONS:
ApiToken or Bearer
QUERY PARAMETERS
string
Default: "all"
Enum: "all"
"official"
"owner"
source
Content type


Filter by OS Image source. Options are:
official : OS Images provided by Genymotion, available to
everyone
owner : OS Images created by authenticated User
all : combination of official & owner
Array of strings
Default: "x86_64,x86"
Items Enum: "x86"
"x86_64"
"arm64"
Filter by the image architecture.
If this isn't specified, x86 and x86_64 will be used by default.
string
Search term to search on name attribute.
integer
Page to fetch
integer
Default: 30
Number of os images per page
Responses
200
A list containing all official and related to the user os images.
401
Not authorized.
500
Service Failed.
Request samples
arch
search
page
page_size
GET
/v1/os-images/


Shell
Python
curl -H 'Content-Type: application/json;charset=utf-8' -H 'x-api-token: <token>
Response samples
200
401
500
Copy
application/json
Expand all
Collapse all
Copy
{
"count": 0,
"results": 
-
[
 … 
+ {
}
]
}
Duplicate an OS Image
This endpoint duplicates an OS Image from the input parameters.
AUTHORIZATIONS:
ApiToken or Bearer
PATH PARAMETERS
string <uuid> ^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][...
Show pattern
Uuid of the OS Image to retrieve
REQUEST BODY SCHEMA: application/json
required
string
OS Image name
Responses
uuid
required
name
required
Content type


201
The duplicated OS Image.
400
Wrong parameters.
401
Not authorized.
403
Not allowed.
500
Service Failed.
Request samples
Payload
Shell
Python
Response samples
201
400
401
403
500
POST
/v1/os-images/{uuid}/duplicate/
application/json
Copy
{
"name": "string"
}
application/json
Expand all
Collapse all
Copy
{
"uuid": "095be615-a8ad-4c33-8e9c-c7612fbf6c9f",
Content type
Content type


Reporting v1
"os_version": 
-
{
"uuid": "095be615-a8ad-4c33-8e9c-c7612fbf6c9f",
"name": "string",
"os_version": "string",
"sdk_version": "string",
"release_date": "string"
},
"parent_os_image_uuid": "cbcb716b-9ff1-4221-877f-79705bbb170e",
"supported_form_factors": 
-
[
"PHONE"
],
"name": "string",
"is_official": true,
"is_beta": true,
"arch": "x86",
"owner": 
-
{
"created_at": 0,
"email": "user@example.com",
"first_name": "string",
"is_enabled": true,
"is_organization_manager": true,
"is_validated": true,
"last_name": "string",
"role": "USER",
"uuid": "095be615-a8ad-4c33-8e9c-c7612fbf6c9f",
"groups":  … 
+
[
],
"organization":  … 
+
{
}
},
"status": "CREATING",
"image_version": "string",
"image_uri": "string",
"image_size_bytes": 0,
"image_hash": "string",
"image_date": "string",
"build_date": "string",
"created_at": "string",
"updated_at": "string",
"recipe_count": 0
}
Get usage report per user for the current
organization.


This endpoint allows an organization's manager to get a usage report for the current
organization.
AUTHORIZATIONS:
ApiToken or Bearer
QUERY PARAMETERS
string <datetime>
Start of the usage period.
string <datetime>
End of the usage period.
Responses
200
Usage report response.
403
The requester isn't allowed to access usage reports.
404
There was no consumption for the given period.
500
Service Failed.
default
An unknown error occurred
Response samples
200
403
404
500
default
from_date
required
to_date
required
GET
/v1/reporting/usage


application/json
Expand all
Collapse all
Copy
{
"count": 0,
"results": 
-
[
 … 
+ {
}
]
}
Content type
