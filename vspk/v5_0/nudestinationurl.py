# -*- coding: utf-8 -*-
#
# Copyright (c) 2015, Alcatel-Lucent Inc
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the copyright holder nor the names of its contributors
#       may be used to endorse or promote products derived from this software without
#       specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.



from .fetchers import NUMetadatasFetcher


from .fetchers import NUGlobalMetadatasFetcher

from bambou import NURESTObject


class NUDestinationurl(NURESTObject):
    """ Represents a Destinationurl in the VSD

        Notes:
            destination URL under tier
    """

    __rest_name__ = "destinationurl"
    __resource_name__ = "destinationurls"

    
    ## Constants
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_HTTP_METHOD_HEAD = "HEAD"
    
    CONST_HTTP_METHOD_GET = "GET"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    

    def __init__(self, **kwargs):
        """ Initializes a Destinationurl instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> destinationurl = NUDestinationurl(id=u'xxxx-xxx-xxx-xxx', name=u'Destinationurl')
                >>> destinationurl = NUDestinationurl(data=my_dict)
        """

        super(NUDestinationurl, self).__init__()

        # Read/Write Attributes
        
        self._url = None
        self._http_method = None
        self._last_updated_by = None
        self._percentage_weight = None
        self._entity_scope = None
        self._down_threshold_count = None
        self._external_id = None
        
        self.expose_attribute(local_name="url", remote_name="URL", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="http_method", remote_name="HTTPMethod", attribute_type=str, is_required=False, is_unique=False, choices=[u'GET', u'HEAD'])
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="percentage_weight", remote_name="percentageWeight", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="down_threshold_count", remote_name="downThresholdCount", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def url(self):
        """ Get url value.

            Notes:
                Uniform Resource Locator

                
                This attribute is named `URL` in VSD API.
                
        """
        return self._url

    @url.setter
    def url(self, value):
        """ Set url value.

            Notes:
                Uniform Resource Locator

                
                This attribute is named `URL` in VSD API.
                
        """
        self._url = value

    
    @property
    def http_method(self):
        """ Get http_method value.

            Notes:
                HTTP probe method (GET/HEAD)

                
                This attribute is named `HTTPMethod` in VSD API.
                
        """
        return self._http_method

    @http_method.setter
    def http_method(self, value):
        """ Set http_method value.

            Notes:
                HTTP probe method (GET/HEAD)

                
                This attribute is named `HTTPMethod` in VSD API.
                
        """
        self._http_method = value

    
    @property
    def last_updated_by(self):
        """ Get last_updated_by value.

            Notes:
                ID of the user who last updated the object.

                
                This attribute is named `lastUpdatedBy` in VSD API.
                
        """
        return self._last_updated_by

    @last_updated_by.setter
    def last_updated_by(self, value):
        """ Set last_updated_by value.

            Notes:
                ID of the user who last updated the object.

                
                This attribute is named `lastUpdatedBy` in VSD API.
                
        """
        self._last_updated_by = value

    
    @property
    def percentage_weight(self):
        """ Get percentage_weight value.

            Notes:
                Weight of the URL in %. Applicable only when parent is Tier1

                
                This attribute is named `percentageWeight` in VSD API.
                
        """
        return self._percentage_weight

    @percentage_weight.setter
    def percentage_weight(self, value):
        """ Set percentage_weight value.

            Notes:
                Weight of the URL in %. Applicable only when parent is Tier1

                
                This attribute is named `percentageWeight` in VSD API.
                
        """
        self._percentage_weight = value

    
    @property
    def entity_scope(self):
        """ Get entity_scope value.

            Notes:
                Specify if scope of entity is Data center or Enterprise level

                
                This attribute is named `entityScope` in VSD API.
                
        """
        return self._entity_scope

    @entity_scope.setter
    def entity_scope(self, value):
        """ Set entity_scope value.

            Notes:
                Specify if scope of entity is Data center or Enterprise level

                
                This attribute is named `entityScope` in VSD API.
                
        """
        self._entity_scope = value

    
    @property
    def down_threshold_count(self):
        """ Get down_threshold_count value.

            Notes:
                Successive Probe threshold. Applicable only if this URL's parent is Tier1

                
                This attribute is named `downThresholdCount` in VSD API.
                
        """
        return self._down_threshold_count

    @down_threshold_count.setter
    def down_threshold_count(self, value):
        """ Set down_threshold_count value.

            Notes:
                Successive Probe threshold. Applicable only if this URL's parent is Tier1

                
                This attribute is named `downThresholdCount` in VSD API.
                
        """
        self._down_threshold_count = value

    
    @property
    def external_id(self):
        """ Get external_id value.

            Notes:
                External object ID. Used for integration with third party systems

                
                This attribute is named `externalID` in VSD API.
                
        """
        return self._external_id

    @external_id.setter
    def external_id(self, value):
        """ Set external_id value.

            Notes:
                External object ID. Used for integration with third party systems

                
                This attribute is named `externalID` in VSD API.
                
        """
        self._external_id = value

    

    