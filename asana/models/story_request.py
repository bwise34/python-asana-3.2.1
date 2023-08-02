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

class StoryRequest(object):
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
        'gid': 'str',
        'resource_type': 'str',
        'created_at': 'datetime',
        'resource_subtype': 'str',
        'text': 'str',
        'html_text': 'str',
        'is_pinned': 'bool',
        'sticker_name': 'str'
    }

    attribute_map = {
        'gid': 'gid',
        'resource_type': 'resource_type',
        'created_at': 'created_at',
        'resource_subtype': 'resource_subtype',
        'text': 'text',
        'html_text': 'html_text',
        'is_pinned': 'is_pinned',
        'sticker_name': 'sticker_name'
    }

    def __init__(self, gid=None, resource_type=None, created_at=None, resource_subtype=None, text=None, html_text=None, is_pinned=None, sticker_name=None):  # noqa: E501
        """StoryRequest - a model defined in Swagger"""  # noqa: E501
        self._gid = None
        self._resource_type = None
        self._created_at = None
        self._resource_subtype = None
        self._text = None
        self._html_text = None
        self._is_pinned = None
        self._sticker_name = None
        self.discriminator = None
        if gid is not None:
            self.gid = gid
        if resource_type is not None:
            self.resource_type = resource_type
        if created_at is not None:
            self.created_at = created_at
        if resource_subtype is not None:
            self.resource_subtype = resource_subtype
        if text is not None:
            self.text = text
        if html_text is not None:
            self.html_text = html_text
        if is_pinned is not None:
            self.is_pinned = is_pinned
        if sticker_name is not None:
            self.sticker_name = sticker_name

    @property
    def gid(self):
        """Gets the gid of this StoryRequest.  # noqa: E501

        Globally unique identifier of the resource, as a string.  # noqa: E501

        :return: The gid of this StoryRequest.  # noqa: E501
        :rtype: str
        """
        return self._gid

    @gid.setter
    def gid(self, gid):
        """Sets the gid of this StoryRequest.

        Globally unique identifier of the resource, as a string.  # noqa: E501

        :param gid: The gid of this StoryRequest.  # noqa: E501
        :type: str
        """

        self._gid = gid

    @property
    def resource_type(self):
        """Gets the resource_type of this StoryRequest.  # noqa: E501

        The base type of this resource.  # noqa: E501

        :return: The resource_type of this StoryRequest.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this StoryRequest.

        The base type of this resource.  # noqa: E501

        :param resource_type: The resource_type of this StoryRequest.  # noqa: E501
        :type: str
        """

        self._resource_type = resource_type

    @property
    def created_at(self):
        """Gets the created_at of this StoryRequest.  # noqa: E501

        The time at which this resource was created.  # noqa: E501

        :return: The created_at of this StoryRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this StoryRequest.

        The time at which this resource was created.  # noqa: E501

        :param created_at: The created_at of this StoryRequest.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def resource_subtype(self):
        """Gets the resource_subtype of this StoryRequest.  # noqa: E501

        The subtype of this resource. Different subtypes retain many of the same fields and behavior, but may render differently in Asana or represent resources with different semantic meaning.  # noqa: E501

        :return: The resource_subtype of this StoryRequest.  # noqa: E501
        :rtype: str
        """
        return self._resource_subtype

    @resource_subtype.setter
    def resource_subtype(self, resource_subtype):
        """Sets the resource_subtype of this StoryRequest.

        The subtype of this resource. Different subtypes retain many of the same fields and behavior, but may render differently in Asana or represent resources with different semantic meaning.  # noqa: E501

        :param resource_subtype: The resource_subtype of this StoryRequest.  # noqa: E501
        :type: str
        """

        self._resource_subtype = resource_subtype

    @property
    def text(self):
        """Gets the text of this StoryRequest.  # noqa: E501

        The plain text of the comment to add. Cannot be used with html_text.  # noqa: E501

        :return: The text of this StoryRequest.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this StoryRequest.

        The plain text of the comment to add. Cannot be used with html_text.  # noqa: E501

        :param text: The text of this StoryRequest.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def html_text(self):
        """Gets the html_text of this StoryRequest.  # noqa: E501

        [Opt In](/docs/inputoutput-options). HTML formatted text for a comment. This will not include the name of the creator.  # noqa: E501

        :return: The html_text of this StoryRequest.  # noqa: E501
        :rtype: str
        """
        return self._html_text

    @html_text.setter
    def html_text(self, html_text):
        """Sets the html_text of this StoryRequest.

        [Opt In](/docs/inputoutput-options). HTML formatted text for a comment. This will not include the name of the creator.  # noqa: E501

        :param html_text: The html_text of this StoryRequest.  # noqa: E501
        :type: str
        """

        self._html_text = html_text

    @property
    def is_pinned(self):
        """Gets the is_pinned of this StoryRequest.  # noqa: E501

        *Conditional*. Whether the story should be pinned on the resource.  # noqa: E501

        :return: The is_pinned of this StoryRequest.  # noqa: E501
        :rtype: bool
        """
        return self._is_pinned

    @is_pinned.setter
    def is_pinned(self, is_pinned):
        """Sets the is_pinned of this StoryRequest.

        *Conditional*. Whether the story should be pinned on the resource.  # noqa: E501

        :param is_pinned: The is_pinned of this StoryRequest.  # noqa: E501
        :type: bool
        """

        self._is_pinned = is_pinned

    @property
    def sticker_name(self):
        """Gets the sticker_name of this StoryRequest.  # noqa: E501

        The name of the sticker in this story. `null` if there is no sticker.  # noqa: E501

        :return: The sticker_name of this StoryRequest.  # noqa: E501
        :rtype: str
        """
        return self._sticker_name

    @sticker_name.setter
    def sticker_name(self, sticker_name):
        """Sets the sticker_name of this StoryRequest.

        The name of the sticker in this story. `null` if there is no sticker.  # noqa: E501

        :param sticker_name: The sticker_name of this StoryRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["green_checkmark", "people_dancing", "dancing_unicorn", "heart", "party_popper", "people_waving_flags", "splashing_narwhal", "trophy", "yeti_riding_unicorn", "celebrating_people", "determined_climbers", "phoenix_spreading_love"]  # noqa: E501
        if sticker_name not in allowed_values:
            raise ValueError(
                "Invalid value for `sticker_name` ({0}), must be one of {1}"  # noqa: E501
                .format(sticker_name, allowed_values)
            )

        self._sticker_name = sticker_name

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
        if issubclass(StoryRequest, dict):
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
        if not isinstance(other, StoryRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other