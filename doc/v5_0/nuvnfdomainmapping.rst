.. _nuvnfdomainmapping:

nuvnfdomainmapping
===========================================

.. class:: nuvnfdomainmapping.NUVNFDomainMapping(bambou.nurest_object.NUMetaRESTObject,):

This represents domain segment identifier which is unique for domain per NSGateway.


Attributes
----------


- ``last_updated_by``: ID of the user who last updated the object.

- ``segmentation_id``: The segmentation ID (1-4095).

- ``segmentation_type``: The type of segmentation that is used.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``associated_ns_gateway_id``: Associated NS Gateway

- ``associated_ns_gateway_name``: Name of associated NSGateway

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nudomain.NUDomain<nudomain>`

