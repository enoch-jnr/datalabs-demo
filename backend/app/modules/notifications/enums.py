from enum import Enum


class NotificationType(str, Enum):
    TASK_ASSIGNED = "TASK_ASSIGNED"
    ANNOTATION_REVIEWED = "ANNOTATION_REVIEWED"
    COMMENT_MENTION = "COMMENT_MENTION"
    PROJECT_UPDATE = "PROJECT_UPDATE"
    SYSTEM_ALERT = "SYSTEM_ALERT"


class NotificationChannel(str, Enum):
    IN_APP = "IN_APP"
    EMAIL = "EMAIL"
    SMS = "SMS"
