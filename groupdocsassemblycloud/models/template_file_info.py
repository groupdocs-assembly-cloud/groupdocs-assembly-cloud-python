# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="TemplateFileInfo.py">
#   Copyright (c) 2020 GroupDocs.Assembly for Cloud
# </copyright>
# <summary>
#   Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
# </summary>
# -----------------------------------------------------------------------------------
import pprint
import re  # noqa: F401

import six


class TemplateFileInfo(object):
    """TemplateFileInfo dto.             
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'file_path': 'str',
        'storage_name': 'str',
        'version_id': 'str',
        'password': 'str'
    }

    attribute_map = {
        'file_path': 'FilePath',
        'storage_name': 'StorageName',
        'version_id': 'VersionId',
        'password': 'Password'
    }

    def __init__(self, file_path=None, storage_name=None, version_id=None, password=None):  # noqa: E501
        """TemplateFileInfo - a model defined in Swagger"""  # noqa: E501

        self._file_path = None
        self._storage_name = None
        self._version_id = None
        self._password = None
        self.discriminator = None

        if file_path is not None:
            self.file_path = file_path
        if storage_name is not None:
            self.storage_name = storage_name
        if version_id is not None:
            self.version_id = version_id
        if password is not None:
            self.password = password

    @property
    def file_path(self):
        """Gets the file_path of this TemplateFileInfo.  # noqa: E501

        Gets or sets path to file.               # noqa: E501

        :return: The file_path of this TemplateFileInfo.  # noqa: E501
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        """Sets the file_path of this TemplateFileInfo.

        Gets or sets path to file.               # noqa: E501

        :param file_path: The file_path of this TemplateFileInfo.  # noqa: E501
        :type: str
        """
        self._file_path = file_path
    @property
    def storage_name(self):
        """Gets the storage_name of this TemplateFileInfo.  # noqa: E501

        Gets or sets the name of storage.               # noqa: E501

        :return: The storage_name of this TemplateFileInfo.  # noqa: E501
        :rtype: str
        """
        return self._storage_name

    @storage_name.setter
    def storage_name(self, storage_name):
        """Sets the storage_name of this TemplateFileInfo.

        Gets or sets the name of storage.               # noqa: E501

        :param storage_name: The storage_name of this TemplateFileInfo.  # noqa: E501
        :type: str
        """
        self._storage_name = storage_name
    @property
    def version_id(self):
        """Gets the version_id of this TemplateFileInfo.  # noqa: E501

        Gets or sets the name of storage.               # noqa: E501

        :return: The version_id of this TemplateFileInfo.  # noqa: E501
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        """Sets the version_id of this TemplateFileInfo.

        Gets or sets the name of storage.               # noqa: E501

        :param version_id: The version_id of this TemplateFileInfo.  # noqa: E501
        :type: str
        """
        self._version_id = version_id
    @property
    def password(self):
        """Gets the password of this TemplateFileInfo.  # noqa: E501

        Gets or sets the password.               # noqa: E501

        :return: The password of this TemplateFileInfo.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this TemplateFileInfo.

        Gets or sets the password.               # noqa: E501

        :param password: The password of this TemplateFileInfo.  # noqa: E501
        :type: str
        """
        self._password = password
    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            alias = attr
            if self.attribute_map[alias]:
                alias = self.attribute_map[alias]
            value = getattr(self, attr)
            if isinstance(value, list):
                result[alias] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[alias] = value.to_dict()
            elif isinstance(value, dict):
                result[alias] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[alias] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TemplateFileInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
