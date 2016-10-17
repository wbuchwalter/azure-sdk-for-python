# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .resource import Resource


class IOSMAMPolicy(Resource):
    """iOS Policy entity for Intune MAM.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param tags: Resource Tags
    :type tags: dict
    :param location: Resource Location
    :type location: str
    :param friendly_name:
    :type friendly_name: str
    :param description:
    :type description: str
    :param app_sharing_from_level: Possible values include: 'none',
     'policyManagedApps', 'allApps'. Default value: "none" .
    :type app_sharing_from_level: str
    :param app_sharing_to_level: Possible values include: 'none',
     'policyManagedApps', 'allApps'. Default value: "none" .
    :type app_sharing_to_level: str
    :param authentication: Possible values include: 'required',
     'notRequired'. Default value: "required" .
    :type authentication: str
    :param clipboard_sharing_level: Possible values include: 'blocked',
     'policyManagedApps', 'policyManagedAppsWithPasteIn', 'allApps'. Default
     value: "blocked" .
    :type clipboard_sharing_level: str
    :param data_backup: Possible values include: 'allow', 'block'. Default
     value: "allow" .
    :type data_backup: str
    :param file_sharing_save_as: Possible values include: 'allow', 'block'.
     Default value: "allow" .
    :type file_sharing_save_as: str
    :param pin: Possible values include: 'required', 'notRequired'. Default
     value: "required" .
    :type pin: str
    :param pin_num_retry:
    :type pin_num_retry: int
    :param device_compliance: Possible values include: 'enable', 'disable'.
     Default value: "enable" .
    :type device_compliance: str
    :param managed_browser: Possible values include: 'required',
     'notRequired'. Default value: "required" .
    :type managed_browser: str
    :param access_recheck_offline_timeout:
    :type access_recheck_offline_timeout: timedelta
    :param access_recheck_online_timeout:
    :type access_recheck_online_timeout: timedelta
    :param offline_wipe_timeout:
    :type offline_wipe_timeout: timedelta
    :ivar num_of_apps:
    :vartype num_of_apps: int
    :ivar group_status: Possible values include: 'notTargeted', 'targeted'.
     Default value: "notTargeted" .
    :vartype group_status: str
    :ivar last_modified_time:
    :vartype last_modified_time: datetime
    :param file_encryption_level: Possible values include: 'deviceLocked',
     'deviceLockedExceptFilesOpen', 'afterDeviceRestart',
     'useDeviceSettings'. Default value: "deviceLocked" .
    :type file_encryption_level: str
    :param touch_id: Possible values include: 'enable', 'disable'. Default
     value: "enable" .
    :type touch_id: str
    """ 

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'friendly_name': {'required': True},
        'num_of_apps': {'readonly': True},
        'group_status': {'readonly': True},
        'last_modified_time': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'friendly_name': {'key': 'properties.friendlyName', 'type': 'str'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'app_sharing_from_level': {'key': 'properties.appSharingFromLevel', 'type': 'str'},
        'app_sharing_to_level': {'key': 'properties.appSharingToLevel', 'type': 'str'},
        'authentication': {'key': 'properties.authentication', 'type': 'str'},
        'clipboard_sharing_level': {'key': 'properties.clipboardSharingLevel', 'type': 'str'},
        'data_backup': {'key': 'properties.dataBackup', 'type': 'str'},
        'file_sharing_save_as': {'key': 'properties.fileSharingSaveAs', 'type': 'str'},
        'pin': {'key': 'properties.pin', 'type': 'str'},
        'pin_num_retry': {'key': 'properties.pinNumRetry', 'type': 'int'},
        'device_compliance': {'key': 'properties.deviceCompliance', 'type': 'str'},
        'managed_browser': {'key': 'properties.managedBrowser', 'type': 'str'},
        'access_recheck_offline_timeout': {'key': 'properties.accessRecheckOfflineTimeout', 'type': 'duration'},
        'access_recheck_online_timeout': {'key': 'properties.accessRecheckOnlineTimeout', 'type': 'duration'},
        'offline_wipe_timeout': {'key': 'properties.offlineWipeTimeout', 'type': 'duration'},
        'num_of_apps': {'key': 'properties.numOfApps', 'type': 'int'},
        'group_status': {'key': 'properties.groupStatus', 'type': 'str'},
        'last_modified_time': {'key': 'properties.lastModifiedTime', 'type': 'iso-8601'},
        'file_encryption_level': {'key': 'properties.fileEncryptionLevel', 'type': 'str'},
        'touch_id': {'key': 'properties.touchId', 'type': 'str'},
    }

    def __init__(self, friendly_name, tags=None, location=None, description=None, app_sharing_from_level="none", app_sharing_to_level="none", authentication="required", clipboard_sharing_level="blocked", data_backup="allow", file_sharing_save_as="allow", pin="required", pin_num_retry=None, device_compliance="enable", managed_browser="required", access_recheck_offline_timeout=None, access_recheck_online_timeout=None, offline_wipe_timeout=None, file_encryption_level="deviceLocked", touch_id="enable"):
        super(IOSMAMPolicy, self).__init__(tags=tags, location=location)
        self.friendly_name = friendly_name
        self.description = description
        self.app_sharing_from_level = app_sharing_from_level
        self.app_sharing_to_level = app_sharing_to_level
        self.authentication = authentication
        self.clipboard_sharing_level = clipboard_sharing_level
        self.data_backup = data_backup
        self.file_sharing_save_as = file_sharing_save_as
        self.pin = pin
        self.pin_num_retry = pin_num_retry
        self.device_compliance = device_compliance
        self.managed_browser = managed_browser
        self.access_recheck_offline_timeout = access_recheck_offline_timeout
        self.access_recheck_online_timeout = access_recheck_online_timeout
        self.offline_wipe_timeout = offline_wipe_timeout
        self.num_of_apps = None
        self.group_status = None
        self.last_modified_time = None
        self.file_encryption_level = file_encryption_level
        self.touch_id = touch_id