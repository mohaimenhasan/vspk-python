.. _nunexthop:

nunexthop
===========================================

.. class:: nunexthop.NUNextHop(bambou.nurest_object.NUMetaRESTObject,):

This represents a /32 IPv4 address as the next-hop. In the future can be a /128 IPv6 address.


Attributes
----------


- ``ip_type``: The IP Type of this Nexthop, possible values are IPV4, IPV6 or DUALSTACK.

- ``last_updated_by``: ID of the user who last updated the object.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``route_distinguisher``: The next-hop's route distinguisher. A unique 8 byte long. If not provided one will be generated.

- ``ip``: This is the /32 or /128 next-hop IP address. Currently we support only IPv4 address family.

- ``external_id``: External object ID. Used for integration with third party systems

- ``type``: Next hop type: IP only supported for service chaining




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nulink.NULink<nulink>`

