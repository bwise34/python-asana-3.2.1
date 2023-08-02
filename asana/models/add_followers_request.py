# coding: utf-8

"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec] (https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AddFollowersRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'followers': 'str'
    }

    attribute_map = {
        'followers': 'followers'
    }

    def __init__(self, followers=None):  # noqa: E501
        """AddFollowersRequest - a model defined in Swagger"""  # noqa: E501
        self._followers = None
        self.discriminator = None
        self.followers = followers

    @property
    def followers(self):
        """Gets the followers of this AddFollowersRequest.  # noqa: E501

        An array of strings identifying users. These can either be the string \"me\", an email, or the gid of a user.  # noqa: E501

        :return: The followers of this AddFollowersRequest.  # noqa: E501
        :rtype: str
        """
        return self._followers

    @followers.setter
    def followers(self, followers):
        """Sets the followers of this AddFollowersRequest.

        An array of strings identifying users. These can either be the string \"me\", an email, or the gid of a user.  # noqa: E501

        :param followers: The followers of this AddFollowersRequest.  # noqa: E501
        :type: str
        """
        if followers is None:
            raise ValueError("Invalid value for `followers`, must not be `None`")  # noqa: E501

        self._followers = followers

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(AddFollowersRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AddFollowersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other