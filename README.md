# Django_DRF

## API
    
    An API( Application Programming Interface) enables two software components to communicate & exchange data with each other using a set of definitions and protocols.
    We define an endpoint to get the list of the students of a particular branch. It is also used on how to make the request and their expected responses.
    
    For ex: Weather Report System contains daily weather data.The weather app on your phone talks to this system via APIs and shows you daily weather updates on your phone.

## REST API: 

    REST(Representational State Transfer):
      
            It is a standardized way to provide data to other applications & is used for building and communicating with web services. 
            
            It is the best way to transfer data across the applications and can be used by the application & mandates resources on the web are represented in JSON,HTML or XML.
            
            Sometimes APIs are used in the other application to change the data. 
            
            The main feature of REST API is statelessness. Statelessness means that servers do not save client data between requests. 
            Client requests to the server are similar to URLs you type in your browser to visit a website. 
            The response from the server is plain data, without the typical graphical rendering of a web page.
        
        Working: 
                A request is sent from client to server in the form of a web URL as HTTP GET or POST or PUT or DELETE request. 
                After that, a response comes back from the server in the form of a resource which can be anything like HTML, XML, Image, or JSON. 
                But now JSON is the most popular format being used in Web Services.
       
        Benefits:
             1. Integration : APIs are used to integrate new applications with existing software systems.
             2. Ease of maintenance: API acts as a gateway between two systems. Each system  requires to make internal changes so that the API is not impacted. 
                                    This way,any future code changes by one party do not impact the other party
             3. Expansion: APIs present a unique opportunity for businesses to meet their clients needs across different platforms. 
                   Ex: maps API allows map information integration via any device. Any business can give similar access to their internal databases by using free or paid APIs.                       
             

## HTTP Methods:

    In HTTP there are five methods that are commonly used in a REST-based Architecture i.e., POST, GET, PUT, PATCH, and DELETE.Additional HEAD,OPTIONS,TRACE etc.
    URI is a Universal Resource Identifier, identifying where a specific resource can be found, such as a page or a document. </h3>
    
    1.GET:  The HTTP GET method is used to read (or retrieve) a representation of a resource.
           In safe path,GET returns representation in XML or JSON and an HTTP response code of 200(OK).In error case, it returns a 404(NOT FOUND) or(BAD REQUEST). 
           
     
    2.POST:  The POST creates new records and updates new created record in the database.
            On successful creation,return HTTP status 201,returning a Location header with a link to the newly-created resource with the 201 HTTP status.
            
           
    3.PUT:   It takes the new records at the given URI. If the record exists, update the record. If record is not available, create a new record.
            On successful update,return 200 (or 204 if not returning any content in the body) from a PUT. 
            If using PUT for create, return HTTP status 201 on successful creation.
            
          
    4.PATCH:  It takes one or more fields at given URI.It is used to update one or more data fields.If record exists,update the record & if not available,create a new record.
   
   
    5.DELETE:  It is used to delete a record at a given URI.On successful deletion, return HTTP status 200 (OK) along with a response body. 
   
   
    6.HEAD:     It is same as GET,but transfers the status line and header section only. 
               HEAD gets the HTTP header you would get if you made a GET request, but without the body.
               
          
    7.OPTIONS: It tells you things such as "What methods are allowed for this resource". 
               It describes the communication options for the target resource.
             
    8.TRACE:   It allows the client to see what is being received at other end of the request chain and use that data for testing or diagnostic information.
               It basically determine what exactly is happening with a request.
               
    9.CONNECT: It starts two-way communications with the requested resource. It can be used to open a tunnel.
               It establishes a tunnel to the server identified by a given URI.
         For ex: CONNECT method can be used to access websites that use SSL(HTTPS).Client asks an HTTP Proxy server to tunnel the TCP connection to desired destination.         
  <a href="https://www.tutorialspoint.com/http/http_methods.htm">For Reference Visit</a>
  
  ## Django REST Framework(DRF):
    
    DRF is a package built on the top of Django to create web APIs.It provides most extensive features of Django,ORM which allows interaction of databases in a Pythonic way.

    Hence Python object can't be sent over network,so we need to translate Django models into the other formats like JSON, XML, and vice-versa.
    This process is known as   serialization, which the Django REST framework made super easy.

    DRF allows us to represent their functionality Django application in the form of REST APIs. It is quite easy to do.
  
  
  ## Serialization & Deserialization:
     
    Serialization allow complex data such as querysets and model instances to be converted to native Python datatypes that can then be easily rendered into JSON, XML or other.
    This makes data lightweight & portable.
    
    Serializers also provide deserialization, allowing parsed data to be converted back into complex types, after first validating the incoming data.
     
  ## Steps to create API using DRF:
    
     1. Add rest_framework to INSTALLED_APPS : To initialize REST Framework in your project, go to settings.py, and in INSTALLED_APPS add ‘rest_framework’ at the bottom. 
        
     2. Create a app and model : To demonstrate, creating and using an API, let’s create a model named “XYZModel” in apis/models.py 
        
     3. Serialization : Converting a Model’s complex data such as querysets and model instances  to JSON/XML format in apis/serializers.py.
        
     4. Creating a viewset : To render data into frontend and handle requests from user, we need to create a view i.e we call Viewset in DRF stored in apis/views.py.
        
     5. Define URLs of API : Creating a URL for mapping to the viewset.Pathway of APIs to be accessed in apis/urls.py
        
     6. Run server and check API: Run following commands to create the database, and run server, 
                                       python manage.py makemigrations
                                       python manage.py migrate
                                       python manage.py runserver


 ## Authentication & Authorization:
      
      ###Authentication: 
                    In Authentication process,the identity of users is checked for providing the access to the system
                    Authentication determines whether the person is user or not basically its verification
                 Ex: Employees in a company are required to authenticate through the network before accessing their company email.    
      
      ###Authorization:  
                   In Authorization process,a person’s or user’s authorities are checked for accessing the resources.
                   While it determines What permission does the user have?, i.e validation of users power
                   It is done after the authentication process.
                 Ex: After an employee successfully authenticates,the system determines what information the employees are allowed to access.
  
  
 ## JWT Authentication:
    
    A JSON web token(JWT) is JSON Object which is used to securely transfer information over the web(between two parties). 
    It can be used for an authentication system and can also be used for information exchange.The token is mainly composed of header, payload, signature. 
   
    JWT is token based stateless auth mechanism.It is a client-side based stateless session, server doesn't have to completely rely on database to save session information.
    
    Structure:
     
      Header:  The header typically consists of two parts i.e  type of token, which is JWT, and signing algorithm being used, such as HMAC SHA256 or RSA.

          Ex:
              {
                 "alg": "HS256",
                 "typ": "JWT"
              }

      Payload: The second part of the token is the payload, which contains the claims. Claims are statements about an entity (typically, the user) and additional data. 
    
          EX:
              {
                   "sub": "1234567890",
                   "name": "John Doe",
                   "admin": true
              }
             
      Signature: The signature is used to verify the message wasn't changed along the way, and, in the case of tokens signed with a private key also verifies sender of  JWT.
