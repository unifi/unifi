#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file has been automatically generated, changes may be lost if you
# go and generate it again. It was generated with the following command:
# manage.py dumpscript

import datetime
from decimal import Decimal
from django.contrib.contenttypes.models import ContentType

def run():
    from django.contrib.auth.models import Permission

    auth_permission_1 = Permission()
    auth_permission_1.name = u'Can add log entry'
    auth_permission_1.content_type = ContentType.objects.get(app_label="admin", model="logentry")
    auth_permission_1.codename = u'add_logentry'
    auth_permission_1.save()

    auth_permission_2 = Permission()
    auth_permission_2.name = u'Can change log entry'
    auth_permission_2.content_type = ContentType.objects.get(app_label="admin", model="logentry")
    auth_permission_2.codename = u'change_logentry'
    auth_permission_2.save()

    auth_permission_3 = Permission()
    auth_permission_3.name = u'Can delete log entry'
    auth_permission_3.content_type = ContentType.objects.get(app_label="admin", model="logentry")
    auth_permission_3.codename = u'delete_logentry'
    auth_permission_3.save()

    auth_permission_4 = Permission()
    auth_permission_4.name = u'Can add group'
    auth_permission_4.content_type = ContentType.objects.get(app_label="auth", model="group")
    auth_permission_4.codename = u'add_group'
    auth_permission_4.save()

    auth_permission_5 = Permission()
    auth_permission_5.name = u'Can change group'
    auth_permission_5.content_type = ContentType.objects.get(app_label="auth", model="group")
    auth_permission_5.codename = u'change_group'
    auth_permission_5.save()

    auth_permission_6 = Permission()
    auth_permission_6.name = u'Can delete group'
    auth_permission_6.content_type = ContentType.objects.get(app_label="auth", model="group")
    auth_permission_6.codename = u'delete_group'
    auth_permission_6.save()

    auth_permission_7 = Permission()
    auth_permission_7.name = u'Can add permission'
    auth_permission_7.content_type = ContentType.objects.get(app_label="auth", model="permission")
    auth_permission_7.codename = u'add_permission'
    auth_permission_7.save()

    auth_permission_8 = Permission()
    auth_permission_8.name = u'Can change permission'
    auth_permission_8.content_type = ContentType.objects.get(app_label="auth", model="permission")
    auth_permission_8.codename = u'change_permission'
    auth_permission_8.save()

    auth_permission_9 = Permission()
    auth_permission_9.name = u'Can delete permission'
    auth_permission_9.content_type = ContentType.objects.get(app_label="auth", model="permission")
    auth_permission_9.codename = u'delete_permission'
    auth_permission_9.save()

    auth_permission_10 = Permission()
    auth_permission_10.name = u'Can add user'
    auth_permission_10.content_type = ContentType.objects.get(app_label="auth", model="user")
    auth_permission_10.codename = u'add_user'
    auth_permission_10.save()

    auth_permission_11 = Permission()
    auth_permission_11.name = u'Can change user'
    auth_permission_11.content_type = ContentType.objects.get(app_label="auth", model="user")
    auth_permission_11.codename = u'change_user'
    auth_permission_11.save()

    auth_permission_12 = Permission()
    auth_permission_12.name = u'Can delete user'
    auth_permission_12.content_type = ContentType.objects.get(app_label="auth", model="user")
    auth_permission_12.codename = u'delete_user'
    auth_permission_12.save()

    auth_permission_13 = Permission()
    auth_permission_13.name = u'Can add message'
    auth_permission_13.content_type = ContentType.objects.get(app_label="communication", model="message")
    auth_permission_13.codename = u'add_message'
    auth_permission_13.save()

    auth_permission_14 = Permission()
    auth_permission_14.name = u'Can change message'
    auth_permission_14.content_type = ContentType.objects.get(app_label="communication", model="message")
    auth_permission_14.codename = u'change_message'
    auth_permission_14.save()

    auth_permission_15 = Permission()
    auth_permission_15.name = u'Can delete message'
    auth_permission_15.content_type = ContentType.objects.get(app_label="communication", model="message")
    auth_permission_15.codename = u'delete_message'
    auth_permission_15.save()

    auth_permission_16 = Permission()
    auth_permission_16.name = u'Can add content type'
    auth_permission_16.content_type = ContentType.objects.get(app_label="contenttypes", model="contenttype")
    auth_permission_16.codename = u'add_contenttype'
    auth_permission_16.save()

    auth_permission_17 = Permission()
    auth_permission_17.name = u'Can change content type'
    auth_permission_17.content_type = ContentType.objects.get(app_label="contenttypes", model="contenttype")
    auth_permission_17.codename = u'change_contenttype'
    auth_permission_17.save()

    auth_permission_18 = Permission()
    auth_permission_18.name = u'Can delete content type'
    auth_permission_18.content_type = ContentType.objects.get(app_label="contenttypes", model="contenttype")
    auth_permission_18.codename = u'delete_contenttype'
    auth_permission_18.save()

    auth_permission_19 = Permission()
    auth_permission_19.name = u'Can add message'
    auth_permission_19.content_type = ContentType.objects.get(app_label="django", model="message")
    auth_permission_19.codename = u'add_message'
    auth_permission_19.save()

    auth_permission_20 = Permission()
    auth_permission_20.name = u'Can change message'
    auth_permission_20.content_type = ContentType.objects.get(app_label="django", model="message")
    auth_permission_20.codename = u'change_message'
    auth_permission_20.save()

    auth_permission_21 = Permission()
    auth_permission_21.name = u'Can delete message'
    auth_permission_21.content_type = ContentType.objects.get(app_label="django", model="message")
    auth_permission_21.codename = u'delete_message'
    auth_permission_21.save()

    auth_permission_22 = Permission()
    auth_permission_22.name = u'Can add queue'
    auth_permission_22.content_type = ContentType.objects.get(app_label="django", model="queue")
    auth_permission_22.codename = u'add_queue'
    auth_permission_22.save()

    auth_permission_23 = Permission()
    auth_permission_23.name = u'Can change queue'
    auth_permission_23.content_type = ContentType.objects.get(app_label="django", model="queue")
    auth_permission_23.codename = u'change_queue'
    auth_permission_23.save()

    auth_permission_24 = Permission()
    auth_permission_24.name = u'Can delete queue'
    auth_permission_24.content_type = ContentType.objects.get(app_label="django", model="queue")
    auth_permission_24.codename = u'delete_queue'
    auth_permission_24.save()

    auth_permission_25 = Permission()
    auth_permission_25.name = u'Can add crontab'
    auth_permission_25.content_type = ContentType.objects.get(app_label="djcelery", model="crontabschedule")
    auth_permission_25.codename = u'add_crontabschedule'
    auth_permission_25.save()

    auth_permission_26 = Permission()
    auth_permission_26.name = u'Can change crontab'
    auth_permission_26.content_type = ContentType.objects.get(app_label="djcelery", model="crontabschedule")
    auth_permission_26.codename = u'change_crontabschedule'
    auth_permission_26.save()

    auth_permission_27 = Permission()
    auth_permission_27.name = u'Can delete crontab'
    auth_permission_27.content_type = ContentType.objects.get(app_label="djcelery", model="crontabschedule")
    auth_permission_27.codename = u'delete_crontabschedule'
    auth_permission_27.save()

    auth_permission_28 = Permission()
    auth_permission_28.name = u'Can add interval'
    auth_permission_28.content_type = ContentType.objects.get(app_label="djcelery", model="intervalschedule")
    auth_permission_28.codename = u'add_intervalschedule'
    auth_permission_28.save()

    auth_permission_29 = Permission()
    auth_permission_29.name = u'Can change interval'
    auth_permission_29.content_type = ContentType.objects.get(app_label="djcelery", model="intervalschedule")
    auth_permission_29.codename = u'change_intervalschedule'
    auth_permission_29.save()

    auth_permission_30 = Permission()
    auth_permission_30.name = u'Can delete interval'
    auth_permission_30.content_type = ContentType.objects.get(app_label="djcelery", model="intervalschedule")
    auth_permission_30.codename = u'delete_intervalschedule'
    auth_permission_30.save()

    auth_permission_31 = Permission()
    auth_permission_31.name = u'Can add periodic task'
    auth_permission_31.content_type = ContentType.objects.get(app_label="djcelery", model="periodictask")
    auth_permission_31.codename = u'add_periodictask'
    auth_permission_31.save()

    auth_permission_32 = Permission()
    auth_permission_32.name = u'Can change periodic task'
    auth_permission_32.content_type = ContentType.objects.get(app_label="djcelery", model="periodictask")
    auth_permission_32.codename = u'change_periodictask'
    auth_permission_32.save()

    auth_permission_33 = Permission()
    auth_permission_33.name = u'Can delete periodic task'
    auth_permission_33.content_type = ContentType.objects.get(app_label="djcelery", model="periodictask")
    auth_permission_33.codename = u'delete_periodictask'
    auth_permission_33.save()

    auth_permission_34 = Permission()
    auth_permission_34.name = u'Can add periodic tasks'
    auth_permission_34.content_type = ContentType.objects.get(app_label="djcelery", model="periodictasks")
    auth_permission_34.codename = u'add_periodictasks'
    auth_permission_34.save()

    auth_permission_35 = Permission()
    auth_permission_35.name = u'Can change periodic tasks'
    auth_permission_35.content_type = ContentType.objects.get(app_label="djcelery", model="periodictasks")
    auth_permission_35.codename = u'change_periodictasks'
    auth_permission_35.save()

    auth_permission_36 = Permission()
    auth_permission_36.name = u'Can delete periodic tasks'
    auth_permission_36.content_type = ContentType.objects.get(app_label="djcelery", model="periodictasks")
    auth_permission_36.codename = u'delete_periodictasks'
    auth_permission_36.save()

    auth_permission_37 = Permission()
    auth_permission_37.name = u'Can add task state'
    auth_permission_37.content_type = ContentType.objects.get(app_label="djcelery", model="taskmeta")
    auth_permission_37.codename = u'add_taskmeta'
    auth_permission_37.save()

    auth_permission_38 = Permission()
    auth_permission_38.name = u'Can change task state'
    auth_permission_38.content_type = ContentType.objects.get(app_label="djcelery", model="taskmeta")
    auth_permission_38.codename = u'change_taskmeta'
    auth_permission_38.save()

    auth_permission_39 = Permission()
    auth_permission_39.name = u'Can delete task state'
    auth_permission_39.content_type = ContentType.objects.get(app_label="djcelery", model="taskmeta")
    auth_permission_39.codename = u'delete_taskmeta'
    auth_permission_39.save()

    auth_permission_40 = Permission()
    auth_permission_40.name = u'Can add saved group result'
    auth_permission_40.content_type = ContentType.objects.get(app_label="djcelery", model="tasksetmeta")
    auth_permission_40.codename = u'add_tasksetmeta'
    auth_permission_40.save()

    auth_permission_41 = Permission()
    auth_permission_41.name = u'Can change saved group result'
    auth_permission_41.content_type = ContentType.objects.get(app_label="djcelery", model="tasksetmeta")
    auth_permission_41.codename = u'change_tasksetmeta'
    auth_permission_41.save()

    auth_permission_42 = Permission()
    auth_permission_42.name = u'Can delete saved group result'
    auth_permission_42.content_type = ContentType.objects.get(app_label="djcelery", model="tasksetmeta")
    auth_permission_42.codename = u'delete_tasksetmeta'
    auth_permission_42.save()

    auth_permission_43 = Permission()
    auth_permission_43.name = u'Can add task'
    auth_permission_43.content_type = ContentType.objects.get(app_label="djcelery", model="taskstate")
    auth_permission_43.codename = u'add_taskstate'
    auth_permission_43.save()

    auth_permission_44 = Permission()
    auth_permission_44.name = u'Can change task'
    auth_permission_44.content_type = ContentType.objects.get(app_label="djcelery", model="taskstate")
    auth_permission_44.codename = u'change_taskstate'
    auth_permission_44.save()

    auth_permission_45 = Permission()
    auth_permission_45.name = u'Can delete task'
    auth_permission_45.content_type = ContentType.objects.get(app_label="djcelery", model="taskstate")
    auth_permission_45.codename = u'delete_taskstate'
    auth_permission_45.save()

    auth_permission_46 = Permission()
    auth_permission_46.name = u'Can add worker'
    auth_permission_46.content_type = ContentType.objects.get(app_label="djcelery", model="workerstate")
    auth_permission_46.codename = u'add_workerstate'
    auth_permission_46.save()

    auth_permission_47 = Permission()
    auth_permission_47.name = u'Can change worker'
    auth_permission_47.content_type = ContentType.objects.get(app_label="djcelery", model="workerstate")
    auth_permission_47.codename = u'change_workerstate'
    auth_permission_47.save()

    auth_permission_48 = Permission()
    auth_permission_48.name = u'Can delete worker'
    auth_permission_48.content_type = ContentType.objects.get(app_label="djcelery", model="workerstate")
    auth_permission_48.codename = u'delete_workerstate'
    auth_permission_48.save()

    auth_permission_49 = Permission()
    auth_permission_49.name = u'Can add github access token'
    auth_permission_49.content_type = ContentType.objects.get(app_label="github", model="githubaccesstoken")
    auth_permission_49.codename = u'add_githubaccesstoken'
    auth_permission_49.save()

    auth_permission_50 = Permission()
    auth_permission_50.name = u'Can change github access token'
    auth_permission_50.content_type = ContentType.objects.get(app_label="github", model="githubaccesstoken")
    auth_permission_50.codename = u'change_githubaccesstoken'
    auth_permission_50.save()

    auth_permission_51 = Permission()
    auth_permission_51.name = u'Can delete github access token'
    auth_permission_51.content_type = ContentType.objects.get(app_label="github", model="githubaccesstoken")
    auth_permission_51.codename = u'delete_githubaccesstoken'
    auth_permission_51.save()

    auth_permission_52 = Permission()
    auth_permission_52.name = u'Can add github profile'
    auth_permission_52.content_type = ContentType.objects.get(app_label="github", model="githubprofile")
    auth_permission_52.codename = u'add_githubprofile'
    auth_permission_52.save()

    auth_permission_53 = Permission()
    auth_permission_53.name = u'Can change github profile'
    auth_permission_53.content_type = ContentType.objects.get(app_label="github", model="githubprofile")
    auth_permission_53.codename = u'change_githubprofile'
    auth_permission_53.save()

    auth_permission_54 = Permission()
    auth_permission_54.name = u'Can delete github profile'
    auth_permission_54.content_type = ContentType.objects.get(app_label="github", model="githubprofile")
    auth_permission_54.codename = u'delete_githubprofile'
    auth_permission_54.save()

    auth_permission_55 = Permission()
    auth_permission_55.name = u'Can add group'
    auth_permission_55.content_type = ContentType.objects.get(app_label="group", model="group")
    auth_permission_55.codename = u'add_group'
    auth_permission_55.save()

    auth_permission_56 = Permission()
    auth_permission_56.name = u'Can change group'
    auth_permission_56.content_type = ContentType.objects.get(app_label="group", model="group")
    auth_permission_56.codename = u'change_group'
    auth_permission_56.save()

    auth_permission_57 = Permission()
    auth_permission_57.name = u'Can delete group'
    auth_permission_57.content_type = ContentType.objects.get(app_label="group", model="group")
    auth_permission_57.codename = u'delete_group'
    auth_permission_57.save()

    auth_permission_58 = Permission()
    auth_permission_58.name = u'Can add role'
    auth_permission_58.content_type = ContentType.objects.get(app_label="group", model="role")
    auth_permission_58.codename = u'add_role'
    auth_permission_58.save()

    auth_permission_59 = Permission()
    auth_permission_59.name = u'Can change role'
    auth_permission_59.content_type = ContentType.objects.get(app_label="group", model="role")
    auth_permission_59.codename = u'change_role'
    auth_permission_59.save()

    auth_permission_60 = Permission()
    auth_permission_60.name = u'Can delete role'
    auth_permission_60.content_type = ContentType.objects.get(app_label="group", model="role")
    auth_permission_60.codename = u'delete_role'
    auth_permission_60.save()

    auth_permission_61 = Permission()
    auth_permission_61.name = u'Can add slot'
    auth_permission_61.content_type = ContentType.objects.get(app_label="group", model="slot")
    auth_permission_61.codename = u'add_slot'
    auth_permission_61.save()

    auth_permission_62 = Permission()
    auth_permission_62.name = u'Can change slot'
    auth_permission_62.content_type = ContentType.objects.get(app_label="group", model="slot")
    auth_permission_62.codename = u'change_slot'
    auth_permission_62.save()

    auth_permission_63 = Permission()
    auth_permission_63.name = u'Can delete slot'
    auth_permission_63.content_type = ContentType.objects.get(app_label="group", model="slot")
    auth_permission_63.codename = u'delete_slot'
    auth_permission_63.save()

    auth_permission_64 = Permission()
    auth_permission_64.name = u'Can add attempt'
    auth_permission_64.content_type = ContentType.objects.get(app_label="login", model="attempt")
    auth_permission_64.codename = u'add_attempt'
    auth_permission_64.save()

    auth_permission_65 = Permission()
    auth_permission_65.name = u'Can change attempt'
    auth_permission_65.content_type = ContentType.objects.get(app_label="login", model="attempt")
    auth_permission_65.codename = u'change_attempt'
    auth_permission_65.save()

    auth_permission_66 = Permission()
    auth_permission_66.name = u'Can delete attempt'
    auth_permission_66.content_type = ContentType.objects.get(app_label="login", model="attempt")
    auth_permission_66.codename = u'delete_attempt'
    auth_permission_66.save()

    auth_permission_67 = Permission()
    auth_permission_67.name = u'Can add banned'
    auth_permission_67.content_type = ContentType.objects.get(app_label="login", model="banned")
    auth_permission_67.codename = u'add_banned'
    auth_permission_67.save()

    auth_permission_68 = Permission()
    auth_permission_68.name = u'Can change banned'
    auth_permission_68.content_type = ContentType.objects.get(app_label="login", model="banned")
    auth_permission_68.codename = u'change_banned'
    auth_permission_68.save()

    auth_permission_69 = Permission()
    auth_permission_69.name = u'Can delete banned'
    auth_permission_69.content_type = ContentType.objects.get(app_label="login", model="banned")
    auth_permission_69.codename = u'delete_banned'
    auth_permission_69.save()

    auth_permission_70 = Permission()
    auth_permission_70.name = u'Can add open id nonce'
    auth_permission_70.content_type = ContentType.objects.get(app_label="openid", model="openidnonce")
    auth_permission_70.codename = u'add_openidnonce'
    auth_permission_70.save()

    auth_permission_71 = Permission()
    auth_permission_71.name = u'Can change open id nonce'
    auth_permission_71.content_type = ContentType.objects.get(app_label="openid", model="openidnonce")
    auth_permission_71.codename = u'change_openidnonce'
    auth_permission_71.save()

    auth_permission_72 = Permission()
    auth_permission_72.name = u'Can delete open id nonce'
    auth_permission_72.content_type = ContentType.objects.get(app_label="openid", model="openidnonce")
    auth_permission_72.codename = u'delete_openidnonce'
    auth_permission_72.save()

    auth_permission_73 = Permission()
    auth_permission_73.name = u'Can add open id profile'
    auth_permission_73.content_type = ContentType.objects.get(app_label="openid", model="openidprofile")
    auth_permission_73.codename = u'add_openidprofile'
    auth_permission_73.save()

    auth_permission_74 = Permission()
    auth_permission_74.name = u'Can change open id profile'
    auth_permission_74.content_type = ContentType.objects.get(app_label="openid", model="openidprofile")
    auth_permission_74.codename = u'change_openidprofile'
    auth_permission_74.save()

    auth_permission_75 = Permission()
    auth_permission_75.name = u'Can delete open id profile'
    auth_permission_75.content_type = ContentType.objects.get(app_label="openid", model="openidprofile")
    auth_permission_75.codename = u'delete_openidprofile'
    auth_permission_75.save()

    auth_permission_76 = Permission()
    auth_permission_76.name = u'Can add open id store'
    auth_permission_76.content_type = ContentType.objects.get(app_label="openid", model="openidstore")
    auth_permission_76.codename = u'add_openidstore'
    auth_permission_76.save()

    auth_permission_77 = Permission()
    auth_permission_77.name = u'Can change open id store'
    auth_permission_77.content_type = ContentType.objects.get(app_label="openid", model="openidstore")
    auth_permission_77.codename = u'change_openidstore'
    auth_permission_77.save()

    auth_permission_78 = Permission()
    auth_permission_78.name = u'Can delete open id store'
    auth_permission_78.content_type = ContentType.objects.get(app_label="openid", model="openidstore")
    auth_permission_78.codename = u'delete_openidstore'
    auth_permission_78.save()

    auth_permission_79 = Permission()
    auth_permission_79.name = u'Can add person'
    auth_permission_79.content_type = ContentType.objects.get(app_label="person", model="person")
    auth_permission_79.codename = u'add_person'
    auth_permission_79.save()

    auth_permission_80 = Permission()
    auth_permission_80.name = u'Can change person'
    auth_permission_80.content_type = ContentType.objects.get(app_label="person", model="person")
    auth_permission_80.codename = u'change_person'
    auth_permission_80.save()

    auth_permission_81 = Permission()
    auth_permission_81.name = u'Can delete person'
    auth_permission_81.content_type = ContentType.objects.get(app_label="person", model="person")
    auth_permission_81.codename = u'delete_person'
    auth_permission_81.save()

    auth_permission_82 = Permission()
    auth_permission_82.name = u'Can add wish'
    auth_permission_82.content_type = ContentType.objects.get(app_label="person", model="wish")
    auth_permission_82.codename = u'add_wish'
    auth_permission_82.save()

    auth_permission_83 = Permission()
    auth_permission_83.name = u'Can change wish'
    auth_permission_83.content_type = ContentType.objects.get(app_label="person", model="wish")
    auth_permission_83.codename = u'change_wish'
    auth_permission_83.save()

    auth_permission_84 = Permission()
    auth_permission_84.name = u'Can delete wish'
    auth_permission_84.content_type = ContentType.objects.get(app_label="person", model="wish")
    auth_permission_84.codename = u'delete_wish'
    auth_permission_84.save()

    auth_permission_85 = Permission()
    auth_permission_85.name = u'Can add session'
    auth_permission_85.content_type = ContentType.objects.get(app_label="sessions", model="session")
    auth_permission_85.codename = u'add_session'
    auth_permission_85.save()

    auth_permission_86 = Permission()
    auth_permission_86.name = u'Can change session'
    auth_permission_86.content_type = ContentType.objects.get(app_label="sessions", model="session")
    auth_permission_86.codename = u'change_session'
    auth_permission_86.save()

    auth_permission_87 = Permission()
    auth_permission_87.name = u'Can delete session'
    auth_permission_87.content_type = ContentType.objects.get(app_label="sessions", model="session")
    auth_permission_87.codename = u'delete_session'
    auth_permission_87.save()

    auth_permission_88 = Permission()
    auth_permission_88.name = u'Can add site'
    auth_permission_88.content_type = ContentType.objects.get(app_label="sites", model="site")
    auth_permission_88.codename = u'add_site'
    auth_permission_88.save()

    auth_permission_89 = Permission()
    auth_permission_89.name = u'Can change site'
    auth_permission_89.content_type = ContentType.objects.get(app_label="sites", model="site")
    auth_permission_89.codename = u'change_site'
    auth_permission_89.save()

    auth_permission_90 = Permission()
    auth_permission_90.name = u'Can delete site'
    auth_permission_90.content_type = ContentType.objects.get(app_label="sites", model="site")
    auth_permission_90.codename = u'delete_site'
    auth_permission_90.save()

    auth_permission_91 = Permission()
    auth_permission_91.name = u'Can add tag'
    auth_permission_91.content_type = ContentType.objects.get(app_label="tag", model="tag")
    auth_permission_91.codename = u'add_tag'
    auth_permission_91.save()

    auth_permission_92 = Permission()
    auth_permission_92.name = u'Can change tag'
    auth_permission_92.content_type = ContentType.objects.get(app_label="tag", model="tag")
    auth_permission_92.codename = u'change_tag'
    auth_permission_92.save()

    auth_permission_93 = Permission()
    auth_permission_93.name = u'Can delete tag'
    auth_permission_93.content_type = ContentType.objects.get(app_label="tag", model="tag")
    auth_permission_93.codename = u'delete_tag'
    auth_permission_93.save()

    auth_permission_94 = Permission()
    auth_permission_94.name = u'Can add twitter access token'
    auth_permission_94.content_type = ContentType.objects.get(app_label="twitter", model="twitteraccesstoken")
    auth_permission_94.codename = u'add_twitteraccesstoken'
    auth_permission_94.save()

    auth_permission_95 = Permission()
    auth_permission_95.name = u'Can change twitter access token'
    auth_permission_95.content_type = ContentType.objects.get(app_label="twitter", model="twitteraccesstoken")
    auth_permission_95.codename = u'change_twitteraccesstoken'
    auth_permission_95.save()

    auth_permission_96 = Permission()
    auth_permission_96.name = u'Can delete twitter access token'
    auth_permission_96.content_type = ContentType.objects.get(app_label="twitter", model="twitteraccesstoken")
    auth_permission_96.codename = u'delete_twitteraccesstoken'
    auth_permission_96.save()

    auth_permission_97 = Permission()
    auth_permission_97.name = u'Can add twitter profile'
    auth_permission_97.content_type = ContentType.objects.get(app_label="twitter", model="twitterprofile")
    auth_permission_97.codename = u'add_twitterprofile'
    auth_permission_97.save()

    auth_permission_98 = Permission()
    auth_permission_98.name = u'Can change twitter profile'
    auth_permission_98.content_type = ContentType.objects.get(app_label="twitter", model="twitterprofile")
    auth_permission_98.codename = u'change_twitterprofile'
    auth_permission_98.save()

    auth_permission_99 = Permission()
    auth_permission_99.name = u'Can delete twitter profile'
    auth_permission_99.content_type = ContentType.objects.get(app_label="twitter", model="twitterprofile")
    auth_permission_99.codename = u'delete_twitterprofile'
    auth_permission_99.save()

    auth_permission_100 = Permission()
    auth_permission_100.name = u'Can add twitter request token'
    auth_permission_100.content_type = ContentType.objects.get(app_label="twitter", model="twitterrequesttoken")
    auth_permission_100.codename = u'add_twitterrequesttoken'
    auth_permission_100.save()

    auth_permission_101 = Permission()
    auth_permission_101.name = u'Can change twitter request token'
    auth_permission_101.content_type = ContentType.objects.get(app_label="twitter", model="twitterrequesttoken")
    auth_permission_101.codename = u'change_twitterrequesttoken'
    auth_permission_101.save()

    auth_permission_102 = Permission()
    auth_permission_102.name = u'Can delete twitter request token'
    auth_permission_102.content_type = ContentType.objects.get(app_label="twitter", model="twitterrequesttoken")
    auth_permission_102.codename = u'delete_twitterrequesttoken'
    auth_permission_102.save()

    from django.contrib.auth.models import Group


    from django.contrib.auth.models import User

    auth_user_1 = User()
    auth_user_1.username = u'ziba'
    auth_user_1.first_name = u''
    auth_user_1.last_name = u''
    auth_user_1.email = u''
    auth_user_1.password = u'sha1$zvxARlfLHKdw$a2d444d486983eb971f5e080acc2a777d10d8db6'
    auth_user_1.is_staff = False
    auth_user_1.is_active = True
    auth_user_1.is_superuser = False
    auth_user_1.last_login = datetime.datetime(2012, 11, 2, 2, 27, 28, 179588, tzinfo=<UTC>)
    auth_user_1.date_joined = datetime.datetime(2012, 11, 2, 2, 27, 28, 179588, tzinfo=<UTC>)
    auth_user_1.save()

    auth_user_2 = User()
    auth_user_2.username = u'yoluv'
    auth_user_2.first_name = u''
    auth_user_2.last_name = u''
    auth_user_2.email = u''
    auth_user_2.password = u'sha1$tr1eWfr8eL14$d0ccf186c0a191aae58c2762733cab96d471e92e'
    auth_user_2.is_staff = False
    auth_user_2.is_active = True
    auth_user_2.is_superuser = False
    auth_user_2.last_login = datetime.datetime(2012, 11, 2, 2, 27, 28, 200977, tzinfo=<UTC>)
    auth_user_2.date_joined = datetime.datetime(2012, 11, 2, 2, 27, 28, 200977, tzinfo=<UTC>)
    auth_user_2.save()

    auth_user_3 = User()
    auth_user_3.username = u'noce'
    auth_user_3.first_name = u''
    auth_user_3.last_name = u''
    auth_user_3.email = u''
    auth_user_3.password = u'sha1$pIphxZSf8zW0$f3fb25633c6a9e641c877ce7dfb58aa64c6ebb73'
    auth_user_3.is_staff = False
    auth_user_3.is_active = True
    auth_user_3.is_superuser = False
    auth_user_3.last_login = datetime.datetime(2012, 11, 2, 2, 27, 28, 210085, tzinfo=<UTC>)
    auth_user_3.date_joined = datetime.datetime(2012, 11, 2, 2, 27, 28, 210085, tzinfo=<UTC>)
    auth_user_3.save()

    auth_user_4 = User()
    auth_user_4.username = u'nefac'
    auth_user_4.first_name = u''
    auth_user_4.last_name = u''
    auth_user_4.email = u''
    auth_user_4.password = u'sha1$efm7bgL0Fjbf$b6c3e5daea11a46bf6dd095754b1e2ba0fe5c72b'
    auth_user_4.is_staff = False
    auth_user_4.is_active = True
    auth_user_4.is_superuser = False
    auth_user_4.last_login = datetime.datetime(2012, 11, 2, 2, 27, 28, 221852, tzinfo=<UTC>)
    auth_user_4.date_joined = datetime.datetime(2012, 11, 2, 2, 27, 28, 221852, tzinfo=<UTC>)
    auth_user_4.save()

    auth_user_5 = User()
    auth_user_5.username = u'hetef'
    auth_user_5.first_name = u''
    auth_user_5.last_name = u''
    auth_user_5.email = u''
    auth_user_5.password = u'sha1$dmWjLRp1lxi7$3306f7605ddf89c1af84e455540c315bbb9b17e4'
    auth_user_5.is_staff = False
    auth_user_5.is_active = True
    auth_user_5.is_superuser = False
    auth_user_5.last_login = datetime.datetime(2012, 11, 2, 2, 27, 28, 232866, tzinfo=<UTC>)
    auth_user_5.date_joined = datetime.datetime(2012, 11, 2, 2, 27, 28, 232866, tzinfo=<UTC>)
    auth_user_5.save()

    auth_user_6 = User()
    auth_user_6.username = u'teh'
    auth_user_6.first_name = u''
    auth_user_6.last_name = u''
    auth_user_6.email = u''
    auth_user_6.password = u'sha1$sGsjP9W0o7eX$bc04f5a3a7d179f61deebb452a04b4a1bf869788'
    auth_user_6.is_staff = False
    auth_user_6.is_active = True
    auth_user_6.is_superuser = False
    auth_user_6.last_login = datetime.datetime(2012, 11, 2, 2, 27, 28, 243588, tzinfo=<UTC>)
    auth_user_6.date_joined = datetime.datetime(2012, 11, 2, 2, 27, 28, 243588, tzinfo=<UTC>)
    auth_user_6.save()

    auth_user_7 = User()
    auth_user_7.username = u'xedin'
    auth_user_7.first_name = u''
    auth_user_7.last_name = u''
    auth_user_7.email = u''
    auth_user_7.password = u'sha1$Kt2HMfCsxjuW$e4a16509b3007274206211cedaaec2daabf62180'
    auth_user_7.is_staff = False
    auth_user_7.is_active = True
    auth_user_7.is_superuser = False
    auth_user_7.last_login = datetime.datetime(2012, 11, 2, 2, 27, 28, 252353, tzinfo=<UTC>)
    auth_user_7.date_joined = datetime.datetime(2012, 11, 2, 2, 27, 28, 252353, tzinfo=<UTC>)
    auth_user_7.save()

    auth_user_8 = User()
    auth_user_8.username = u'nocoh'
    auth_user_8.first_name = u''
    auth_user_8.last_name = u''
    auth_user_8.email = u''
    auth_user_8.password = u'sha1$RzxjORZ4IvZs$6035efe5e2762138500e53cb526486a855b76186'
    auth_user_8.is_staff = False
    auth_user_8.is_active = True
    auth_user_8.is_superuser = False
    auth_user_8.last_login = datetime.datetime(2012, 11, 2, 2, 27, 28, 261322, tzinfo=<UTC>)
    auth_user_8.date_joined = datetime.datetime(2012, 11, 2, 2, 27, 28, 261322, tzinfo=<UTC>)
    auth_user_8.save()

    auth_user_9 = User()
    auth_user_9.username = u'lesay'
    auth_user_9.first_name = u''
    auth_user_9.last_name = u''
    auth_user_9.email = u''
    auth_user_9.password = u'sha1$DmG39pg2abG8$0fecb6256c6dfd49c186b9c793e005197f0a6831'
    auth_user_9.is_staff = False
    auth_user_9.is_active = True
    auth_user_9.is_superuser = False
    auth_user_9.last_login = datetime.datetime(2012, 11, 2, 2, 27, 28, 270395, tzinfo=<UTC>)
    auth_user_9.date_joined = datetime.datetime(2012, 11, 2, 2, 27, 28, 270395, tzinfo=<UTC>)
    auth_user_9.save()

    auth_user_10 = User()
    auth_user_10.username = u'yikaf'
    auth_user_10.first_name = u''
    auth_user_10.last_name = u''
    auth_user_10.email = u''
    auth_user_10.password = u'sha1$fdLVmIFhyGN0$24ab8532aeeb856afdc966892d489a3ccf819a85'
    auth_user_10.is_staff = False
    auth_user_10.is_active = True
    auth_user_10.is_superuser = False
    auth_user_10.last_login = datetime.datetime(2012, 11, 2, 2, 27, 28, 279051, tzinfo=<UTC>)
    auth_user_10.date_joined = datetime.datetime(2012, 11, 2, 2, 27, 28, 279051, tzinfo=<UTC>)
    auth_user_10.save()

    auth_user_11 = User()
    auth_user_11.username = u'xuber'
    auth_user_11.first_name = u''
    auth_user_11.last_name = u''
    auth_user_11.email = u''
    auth_user_11.password = u'sha1$wFEsZoznApXr$d2b13e34756c62783822ec12c5f039919454a6b0'
    auth_user_11.is_staff = False
    auth_user_11.is_active = True
    auth_user_11.is_superuser = False
    auth_user_11.last_login = datetime.datetime(2012, 11, 2, 2, 27, 28, 287833, tzinfo=<UTC>)
    auth_user_11.date_joined = datetime.datetime(2012, 11, 2, 2, 27, 28, 287833, tzinfo=<UTC>)
    auth_user_11.save()

    auth_user_12 = User()
    auth_user_12.username = u'coni'
    auth_user_12.first_name = u''
    auth_user_12.last_name = u''
    auth_user_12.email = u''
    auth_user_12.password = u'sha1$pOlfvyAoxpkD$ced1cb137e5148068579015ba3dbe25c54953903'
    auth_user_12.is_staff = False
    auth_user_12.is_active = True
    auth_user_12.is_superuser = False
    auth_user_12.last_login = datetime.datetime(2012, 11, 2, 2, 27, 28, 296887, tzinfo=<UTC>)
    auth_user_12.date_joined = datetime.datetime(2012, 11, 2, 2, 27, 28, 296887, tzinfo=<UTC>)
    auth_user_12.save()

    auth_user_13 = User()
    auth_user_13.username = u'pani'
    auth_user_13.first_name = u''
    auth_user_13.last_name = u''
    auth_user_13.email = u''
    auth_user_13.password = u'sha1$64b90h9cT2JN$90c651978d967d7537cbbf90930cff986034f6a5'
    auth_user_13.is_staff = False
    auth_user_13.is_active = True
    auth_user_13.is_superuser = False
    auth_user_13.last_login = datetime.datetime(2012, 11, 2, 2, 27, 28, 305962, tzinfo=<UTC>)
    auth_user_13.date_joined = datetime.datetime(2012, 11, 2, 2, 27, 28, 305962, tzinfo=<UTC>)
    auth_user_13.save()

    auth_user_14 = User()
    auth_user_14.username = u'sis'
    auth_user_14.first_name = u''
    auth_user_14.last_name = u''
    auth_user_14.email = u''
    auth_user_14.password = u'sha1$O2AV0RWhak8T$69d5a7d0e2dced67a9b52af9c7a25d0339257842'
    auth_user_14.is_staff = False
    auth_user_14.is_active = True
    auth_user_14.is_superuser = False
    auth_user_14.last_login = datetime.datetime(2012, 11, 2, 2, 27, 28, 315136, tzinfo=<UTC>)
    auth_user_14.date_joined = datetime.datetime(2012, 11, 2, 2, 27, 28, 315136, tzinfo=<UTC>)
    auth_user_14.save()

    auth_user_15 = User()
    auth_user_15.username = u'ziqik'
    auth_user_15.first_name = u''
    auth_user_15.last_name = u''
    auth_user_15.email = u''
    auth_user_15.password = u'sha1$STHMzKt0xloH$565a5000755755c584ba0754abc71c849481c765'
    auth_user_15.is_staff = False
    auth_user_15.is_active = True
    auth_user_15.is_superuser = False
    auth_user_15.last_login = datetime.datetime(2012, 11, 2, 2, 27, 28, 324445, tzinfo=<UTC>)
    auth_user_15.date_joined = datetime.datetime(2012, 11, 2, 2, 27, 28, 324445, tzinfo=<UTC>)
    auth_user_15.save()

    auth_user_16 = User()
    auth_user_16.username = u'mik'
    auth_user_16.first_name = u''
    auth_user_16.last_name = u''
    auth_user_16.email = u''
    auth_user_16.password = u'sha1$S2uKpOGuyKoT$ab2248573a2108931ba5bfda59b9ef3332143aec'
    auth_user_16.is_staff = False
    auth_user_16.is_active = True
    auth_user_16.is_superuser = False
    auth_user_16.last_login = datetime.datetime(2012, 11, 2, 2, 27, 28, 333418, tzinfo=<UTC>)
    auth_user_16.date_joined = datetime.datetime(2012, 11, 2, 2, 27, 28, 333418, tzinfo=<UTC>)
    auth_user_16.save()

    auth_user_17 = User()
    auth_user_17.username = u'macus'
    auth_user_17.first_name = u''
    auth_user_17.last_name = u''
    auth_user_17.email = u''
    auth_user_17.password = u'sha1$5Qg0e0fGtzGS$15462d3db435abc1fdb586715a5a10ef5cf83bc9'
    auth_user_17.is_staff = False
    auth_user_17.is_active = True
    auth_user_17.is_superuser = False
    auth_user_17.last_login = datetime.datetime(2012, 11, 2, 2, 27, 28, 343104, tzinfo=<UTC>)
    auth_user_17.date_joined = datetime.datetime(2012, 11, 2, 2, 27, 28, 343104, tzinfo=<UTC>)
    auth_user_17.save()

    auth_user_18 = User()
    auth_user_18.username = u'qas'
    auth_user_18.first_name = u''
    auth_user_18.last_name = u''
    auth_user_18.email = u''
    auth_user_18.password = u'sha1$ynVfF04V0Ser$e4680d0b6ae731ed0f7a3635624d66e39205371f'
    auth_user_18.is_staff = False
    auth_user_18.is_active = True
    auth_user_18.is_superuser = False
    auth_user_18.last_login = datetime.datetime(2012, 11, 2, 2, 27, 28, 354638, tzinfo=<UTC>)
    auth_user_18.date_joined = datetime.datetime(2012, 11, 2, 2, 27, 28, 354638, tzinfo=<UTC>)
    auth_user_18.save()

    auth_user_19 = User()
    auth_user_19.username = u'lux'
    auth_user_19.first_name = u''
    auth_user_19.last_name = u''
    auth_user_19.email = u''
    auth_user_19.password = u'sha1$YOQ3dUdOu2VS$0539fff2706d6ba4069bb5158846a307fc40ed55'
    auth_user_19.is_staff = False
    auth_user_19.is_active = True
    auth_user_19.is_superuser = False
    auth_user_19.last_login = datetime.datetime(2012, 11, 2, 2, 27, 28, 364210, tzinfo=<UTC>)
    auth_user_19.date_joined = datetime.datetime(2012, 11, 2, 2, 27, 28, 364210, tzinfo=<UTC>)
    auth_user_19.save()

    auth_user_20 = User()
    auth_user_20.username = u'dupot'
    auth_user_20.first_name = u''
    auth_user_20.last_name = u''
    auth_user_20.email = u''
    auth_user_20.password = u'sha1$Xt2XNAxem3gw$9a7ef8dc0a88cd452323dc749a1bea2d2384ed83'
    auth_user_20.is_staff = False
    auth_user_20.is_active = True
    auth_user_20.is_superuser = False
    auth_user_20.last_login = datetime.datetime(2012, 11, 2, 2, 27, 28, 373890, tzinfo=<UTC>)
    auth_user_20.date_joined = datetime.datetime(2012, 11, 2, 2, 27, 28, 373890, tzinfo=<UTC>)
    auth_user_20.save()

    auth_user_21 = User()
    auth_user_21.username = u'kup'
    auth_user_21.first_name = u''
    auth_user_21.last_name = u''
    auth_user_21.email = u''
    auth_user_21.password = u'sha1$odk4aUZOiHOk$1c7f3af250ff111c4863acc82b81ab3edca34cff'
    auth_user_21.is_staff = False
    auth_user_21.is_active = True
    auth_user_21.is_superuser = False
    auth_user_21.last_login = datetime.datetime(2012, 11, 2, 2, 27, 28, 382978, tzinfo=<UTC>)
    auth_user_21.date_joined = datetime.datetime(2012, 11, 2, 2, 27, 28, 382978, tzinfo=<UTC>)
    auth_user_21.save()

    auth_user_22 = User()
    auth_user_22.username = u'jesex'
    auth_user_22.first_name = u''
    auth_user_22.last_name = u''
    auth_user_22.email = u''
    auth_user_22.password = u'sha1$4P6JQz4ygYaR$5379f57583496731c399e6ab53a018e166324470'
    auth_user_22.is_staff = False
    auth_user_22.is_active = True
    auth_user_22.is_superuser = False
    auth_user_22.last_login = datetime.datetime(2012, 11, 2, 2, 27, 28, 392493, tzinfo=<UTC>)
    auth_user_22.date_joined = datetime.datetime(2012, 11, 2, 2, 27, 28, 392493, tzinfo=<UTC>)
    auth_user_22.save()

    auth_user_23 = User()
    auth_user_23.username = u'xiv'
    auth_user_23.first_name = u''
    auth_user_23.last_name = u''
    auth_user_23.email = u''
    auth_user_23.password = u'sha1$UlHfwufyBRmx$f7862345971c73b047c166ef1b9ac78fe0579072'
    auth_user_23.is_staff = False
    auth_user_23.is_active = True
    auth_user_23.is_superuser = False
    auth_user_23.last_login = datetime.datetime(2012, 11, 2, 2, 27, 28, 402605, tzinfo=<UTC>)
    auth_user_23.date_joined = datetime.datetime(2012, 11, 2, 2, 27, 28, 402605, tzinfo=<UTC>)
    auth_user_23.save()

    auth_user_24 = User()
    auth_user_24.username = u'feq'
    auth_user_24.first_name = u''
    auth_user_24.last_name = u''
    auth_user_24.email = u''
    auth_user_24.password = u'sha1$pFEDgTmf6n8m$b3b3bd0d6270b1c4cfb0758dbb4eaa8fb8b3eec6'
    auth_user_24.is_staff = False
    auth_user_24.is_active = True
    auth_user_24.is_superuser = False
    auth_user_24.last_login = datetime.datetime(2012, 11, 2, 2, 27, 28, 411378, tzinfo=<UTC>)
    auth_user_24.date_joined = datetime.datetime(2012, 11, 2, 2, 27, 28, 411378, tzinfo=<UTC>)
    auth_user_24.save()

    auth_user_25 = User()
    auth_user_25.username = u'var'
    auth_user_25.first_name = u''
    auth_user_25.last_name = u''
    auth_user_25.email = u''
    auth_user_25.password = u'sha1$7KDEIRrcyqs9$affc6efb3af7f0a981d0c1e820053ce4f0edab89'
    auth_user_25.is_staff = False
    auth_user_25.is_active = True
    auth_user_25.is_superuser = False
    auth_user_25.last_login = datetime.datetime(2012, 11, 2, 2, 27, 28, 420598, tzinfo=<UTC>)
    auth_user_25.date_joined = datetime.datetime(2012, 11, 2, 2, 27, 28, 420598, tzinfo=<UTC>)
    auth_user_25.save()

    auth_user_26 = User()
    auth_user_26.username = u'tig'
    auth_user_26.first_name = u''
    auth_user_26.last_name = u''
    auth_user_26.email = u''
    auth_user_26.password = u'sha1$E5ILebLx3Na0$3a216e66696e1ae0920a66a0491722eaa200903e'
    auth_user_26.is_staff = False
    auth_user_26.is_active = True
    auth_user_26.is_superuser = False
    auth_user_26.last_login = datetime.datetime(2012, 11, 2, 2, 27, 28, 430265, tzinfo=<UTC>)
    auth_user_26.date_joined = datetime.datetime(2012, 11, 2, 2, 27, 28, 430265, tzinfo=<UTC>)
    auth_user_26.save()

    auth_user_27 = User()
    auth_user_27.username = u'jero'
    auth_user_27.first_name = u''
    auth_user_27.last_name = u''
    auth_user_27.email = u''
    auth_user_27.password = u'sha1$U4kpykiYhrpu$28e772584ac1d2511408fe9c5b362589ade7dac9'
    auth_user_27.is_staff = False
    auth_user_27.is_active = True
    auth_user_27.is_superuser = False
    auth_user_27.last_login = datetime.datetime(2012, 11, 2, 2, 27, 28, 438987, tzinfo=<UTC>)
    auth_user_27.date_joined = datetime.datetime(2012, 11, 2, 2, 27, 28, 438987, tzinfo=<UTC>)
    auth_user_27.save()

    auth_user_28 = User()
    auth_user_28.username = u'suf'
    auth_user_28.first_name = u''
    auth_user_28.last_name = u''
    auth_user_28.email = u''
    auth_user_28.password = u'sha1$qvzT7DvaVeoA$6b3f43c394f032a715497172b319892ce7bf9cf6'
    auth_user_28.is_staff = False
    auth_user_28.is_active = True
    auth_user_28.is_superuser = False
    auth_user_28.last_login = datetime.datetime(2012, 11, 2, 2, 27, 28, 448772, tzinfo=<UTC>)
    auth_user_28.date_joined = datetime.datetime(2012, 11, 2, 2, 27, 28, 448772, tzinfo=<UTC>)
    auth_user_28.save()

    auth_user_29 = User()
    auth_user_29.username = u'cokec'
    auth_user_29.first_name = u''
    auth_user_29.last_name = u''
    auth_user_29.email = u''
    auth_user_29.password = u'sha1$DQvifaNpdbrk$f231c98772d1b176638c5bb970caeea911266935'
    auth_user_29.is_staff = False
    auth_user_29.is_active = True
    auth_user_29.is_superuser = False
    auth_user_29.last_login = datetime.datetime(2012, 11, 2, 2, 27, 28, 457860, tzinfo=<UTC>)
    auth_user_29.date_joined = datetime.datetime(2012, 11, 2, 2, 27, 28, 457860, tzinfo=<UTC>)
    auth_user_29.save()

    auth_user_30 = User()
    auth_user_30.username = u'vones'
    auth_user_30.first_name = u''
    auth_user_30.last_name = u''
    auth_user_30.email = u''
    auth_user_30.password = u'sha1$VW5YMMCfKVxM$d15a71e59dd8df22cc3688c6bfc4fd8f20f5cc0b'
    auth_user_30.is_staff = False
    auth_user_30.is_active = True
    auth_user_30.is_superuser = False
    auth_user_30.last_login = datetime.datetime(2012, 11, 2, 2, 27, 28, 466421, tzinfo=<UTC>)
    auth_user_30.date_joined = datetime.datetime(2012, 11, 2, 2, 27, 28, 466421, tzinfo=<UTC>)
    auth_user_30.save()

    auth_user_31 = User()
    auth_user_31.username = u'poxo'
    auth_user_31.first_name = u''
    auth_user_31.last_name = u''
    auth_user_31.email = u''
    auth_user_31.password = u'sha1$NXaye9TtqH3Z$fed90d6914832aefc78d0a066a51f0ac24ec8acd'
    auth_user_31.is_staff = False
    auth_user_31.is_active = True
    auth_user_31.is_superuser = False
    auth_user_31.last_login = datetime.datetime(2012, 11, 2, 2, 27, 28, 475774, tzinfo=<UTC>)
    auth_user_31.date_joined = datetime.datetime(2012, 11, 2, 2, 27, 28, 475774, tzinfo=<UTC>)
    auth_user_31.save()

    auth_user_32 = User()
    auth_user_32.username = u'kij'
    auth_user_32.first_name = u''
    auth_user_32.last_name = u''
    auth_user_32.email = u''
    auth_user_32.password = u'sha1$foOkPYxy8AHu$98a11060a3251d7bdfe1f251baf31c2200a5171f'
    auth_user_32.is_staff = False
    auth_user_32.is_active = True
    auth_user_32.is_superuser = False
    auth_user_32.last_login = datetime.datetime(2012, 11, 2, 2, 27, 28, 484265, tzinfo=<UTC>)
    auth_user_32.date_joined = datetime.datetime(2012, 11, 2, 2, 27, 28, 484265, tzinfo=<UTC>)
    auth_user_32.save()

    auth_user_33 = User()
    auth_user_33.username = u'deqi'
    auth_user_33.first_name = u''
    auth_user_33.last_name = u''
    auth_user_33.email = u''
    auth_user_33.password = u'sha1$UoZVeJrPkNwt$fc2ae556676cf6dd942a8be9a5babd9cb0c11760'
    auth_user_33.is_staff = False
    auth_user_33.is_active = True
    auth_user_33.is_superuser = False
    auth_user_33.last_login = datetime.datetime(2012, 11, 2, 2, 27, 28, 494589, tzinfo=<UTC>)
    auth_user_33.date_joined = datetime.datetime(2012, 11, 2, 2, 27, 28, 494589, tzinfo=<UTC>)
    auth_user_33.save()

    auth_user_34 = User()
    auth_user_34.username = u'pex'
    auth_user_34.first_name = u''
    auth_user_34.last_name = u''
    auth_user_34.email = u''
    auth_user_34.password = u'sha1$BCUZSs9kyUDw$c9fc4fbd2338c0b93dadd9c0a92e63943600c93b'
    auth_user_34.is_staff = False
    auth_user_34.is_active = True
    auth_user_34.is_superuser = False
    auth_user_34.last_login = datetime.datetime(2012, 11, 2, 2, 27, 28, 503408, tzinfo=<UTC>)
    auth_user_34.date_joined = datetime.datetime(2012, 11, 2, 2, 27, 28, 503408, tzinfo=<UTC>)
    auth_user_34.save()

    auth_user_35 = User()
    auth_user_35.username = u'cuje'
    auth_user_35.first_name = u''
    auth_user_35.last_name = u''
    auth_user_35.email = u''
    auth_user_35.password = u'sha1$KjgdwAucK1zA$e2122cf71c3d9a40ac3caafaec1d6eb91f209300'
    auth_user_35.is_staff = False
    auth_user_35.is_active = True
    auth_user_35.is_superuser = False
    auth_user_35.last_login = datetime.datetime(2012, 11, 2, 2, 27, 28, 512037, tzinfo=<UTC>)
    auth_user_35.date_joined = datetime.datetime(2012, 11, 2, 2, 27, 28, 512037, tzinfo=<UTC>)
    auth_user_35.save()

    auth_user_36 = User()
    auth_user_36.username = u'yugo'
    auth_user_36.first_name = u''
    auth_user_36.last_name = u''
    auth_user_36.email = u''
    auth_user_36.password = u'sha1$VXWgzNosvvNJ$f849927f2e883fcd24eac800bd9676c703a1450e'
    auth_user_36.is_staff = False
    auth_user_36.is_active = True
    auth_user_36.is_superuser = False
    auth_user_36.last_login = datetime.datetime(2012, 11, 2, 2, 27, 28, 520708, tzinfo=<UTC>)
    auth_user_36.date_joined = datetime.datetime(2012, 11, 2, 2, 27, 28, 520708, tzinfo=<UTC>)
    auth_user_36.save()

    auth_user_37 = User()
    auth_user_37.username = u'bule'
    auth_user_37.first_name = u''
    auth_user_37.last_name = u''
    auth_user_37.email = u''
    auth_user_37.password = u'sha1$hdIX69oCMucv$95b66da4aeb16bcc5881678dfd5634b4c53fe81c'
    auth_user_37.is_staff = False
    auth_user_37.is_active = True
    auth_user_37.is_superuser = False
    auth_user_37.last_login = datetime.datetime(2012, 11, 2, 2, 27, 28, 529281, tzinfo=<UTC>)
    auth_user_37.date_joined = datetime.datetime(2012, 11, 2, 2, 27, 28, 529281, tzinfo=<UTC>)
    auth_user_37.save()

    auth_user_38 = User()
    auth_user_38.username = u'qocez'
    auth_user_38.first_name = u''
    auth_user_38.last_name = u''
    auth_user_38.email = u''
    auth_user_38.password = u'sha1$OnaT7AFhjPgo$0114e82e058fe0deb7e37ec8d102fa6b5767321e'
    auth_user_38.is_staff = False
    auth_user_38.is_active = True
    auth_user_38.is_superuser = False
    auth_user_38.last_login = datetime.datetime(2012, 11, 2, 2, 27, 28, 537816, tzinfo=<UTC>)
    auth_user_38.date_joined = datetime.datetime(2012, 11, 2, 2, 27, 28, 537816, tzinfo=<UTC>)
    auth_user_38.save()

    auth_user_39 = User()
    auth_user_39.username = u'xuv'
    auth_user_39.first_name = u''
    auth_user_39.last_name = u''
    auth_user_39.email = u''
    auth_user_39.password = u'sha1$yLRF9k9JEnJh$53187b61a8ce63ead79851412b9df46974bee1aa'
    auth_user_39.is_staff = False
    auth_user_39.is_active = True
    auth_user_39.is_superuser = False
    auth_user_39.last_login = datetime.datetime(2012, 11, 2, 2, 27, 28, 546538, tzinfo=<UTC>)
    auth_user_39.date_joined = datetime.datetime(2012, 11, 2, 2, 27, 28, 546538, tzinfo=<UTC>)
    auth_user_39.save()

    auth_user_40 = User()
    auth_user_40.username = u'kexeg'
    auth_user_40.first_name = u''
    auth_user_40.last_name = u''
    auth_user_40.email = u''
    auth_user_40.password = u'sha1$e2Kt2Um7YSTN$cc0e4b8aa611949efb4f5fd2b95b29f33c57c856'
    auth_user_40.is_staff = False
    auth_user_40.is_active = True
    auth_user_40.is_superuser = False
    auth_user_40.last_login = datetime.datetime(2012, 11, 2, 2, 27, 28, 556141, tzinfo=<UTC>)
    auth_user_40.date_joined = datetime.datetime(2012, 11, 2, 2, 27, 28, 556141, tzinfo=<UTC>)
    auth_user_40.save()

    auth_user_41 = User()
    auth_user_41.username = u'deroh'
    auth_user_41.first_name = u''
    auth_user_41.last_name = u''
    auth_user_41.email = u''
    auth_user_41.password = u'sha1$Dju0VpGUIuKx$4bd34cdbf46111d64c0c3484eeb046cb85620603'
    auth_user_41.is_staff = False
    auth_user_41.is_active = True
    auth_user_41.is_superuser = False
    auth_user_41.last_login = datetime.datetime(2012, 11, 2, 2, 27, 28, 564777, tzinfo=<UTC>)
    auth_user_41.date_joined = datetime.datetime(2012, 11, 2, 2, 27, 28, 564777, tzinfo=<UTC>)
    auth_user_41.save()

    auth_user_42 = User()
    auth_user_42.username = u'behak'
    auth_user_42.first_name = u''
    auth_user_42.last_name = u''
    auth_user_42.email = u''
    auth_user_42.password = u'sha1$msZoqPF3okxR$6a77f1d2bbb67a35e06df5ae0334432e12d87be8'
    auth_user_42.is_staff = False
    auth_user_42.is_active = True
    auth_user_42.is_superuser = False
    auth_user_42.last_login = datetime.datetime(2012, 11, 2, 2, 27, 28, 573239, tzinfo=<UTC>)
    auth_user_42.date_joined = datetime.datetime(2012, 11, 2, 2, 27, 28, 573239, tzinfo=<UTC>)
    auth_user_42.save()

    auth_user_43 = User()
    auth_user_43.username = u'bec'
    auth_user_43.first_name = u''
    auth_user_43.last_name = u''
    auth_user_43.email = u''
    auth_user_43.password = u'sha1$1TBnaR1raI1q$90de62e2cebeb1e9f923538485201da871fe861f'
    auth_user_43.is_staff = False
    auth_user_43.is_active = True
    auth_user_43.is_superuser = False
    auth_user_43.last_login = datetime.datetime(2012, 11, 2, 2, 27, 28, 581868, tzinfo=<UTC>)
    auth_user_43.date_joined = datetime.datetime(2012, 11, 2, 2, 27, 28, 581868, tzinfo=<UTC>)
    auth_user_43.save()

    auth_user_44 = User()
    auth_user_44.username = u'dikob'
    auth_user_44.first_name = u''
    auth_user_44.last_name = u''
    auth_user_44.email = u''
    auth_user_44.password = u'sha1$xPK05xTldzhT$644562305416f6e34373e4b0624d4e82bab496ec'
    auth_user_44.is_staff = False
    auth_user_44.is_active = True
    auth_user_44.is_superuser = False
    auth_user_44.last_login = datetime.datetime(2012, 11, 2, 2, 27, 28, 590365, tzinfo=<UTC>)
    auth_user_44.date_joined = datetime.datetime(2012, 11, 2, 2, 27, 28, 590365, tzinfo=<UTC>)
    auth_user_44.save()

    auth_user_45 = User()
    auth_user_45.username = u'zatip'
    auth_user_45.first_name = u''
    auth_user_45.last_name = u''
    auth_user_45.email = u''
    auth_user_45.password = u'sha1$b2kWKwxIp4QK$8dba2abd82b66c1ad69b60a2c3f85ac059cac6b7'
    auth_user_45.is_staff = False
    auth_user_45.is_active = True
    auth_user_45.is_superuser = False
    auth_user_45.last_login = datetime.datetime(2012, 11, 2, 2, 27, 28, 599695, tzinfo=<UTC>)
    auth_user_45.date_joined = datetime.datetime(2012, 11, 2, 2, 27, 28, 599695, tzinfo=<UTC>)
    auth_user_45.save()

    auth_user_46 = User()
    auth_user_46.username = u'lowax'
    auth_user_46.first_name = u''
    auth_user_46.last_name = u''
    auth_user_46.email = u''
    auth_user_46.password = u'sha1$2rbX7roqcC4U$31ecf8cc7cdacc01206398fa118b6526799ba833'
    auth_user_46.is_staff = False
    auth_user_46.is_active = True
    auth_user_46.is_superuser = False
    auth_user_46.last_login = datetime.datetime(2012, 11, 2, 2, 27, 28, 608885, tzinfo=<UTC>)
    auth_user_46.date_joined = datetime.datetime(2012, 11, 2, 2, 27, 28, 608885, tzinfo=<UTC>)
    auth_user_46.save()

    auth_user_47 = User()
    auth_user_47.username = u'xasay'
    auth_user_47.first_name = u''
    auth_user_47.last_name = u''
    auth_user_47.email = u''
    auth_user_47.password = u'sha1$q8pToIZg2BdU$0bbb449d9e15a8160855ba12bae24912ce9cb684'
    auth_user_47.is_staff = False
    auth_user_47.is_active = True
    auth_user_47.is_superuser = False
    auth_user_47.last_login = datetime.datetime(2012, 11, 2, 2, 27, 28, 617774, tzinfo=<UTC>)
    auth_user_47.date_joined = datetime.datetime(2012, 11, 2, 2, 27, 28, 617774, tzinfo=<UTC>)
    auth_user_47.save()

    auth_user_48 = User()
    auth_user_48.username = u'nowu'
    auth_user_48.first_name = u''
    auth_user_48.last_name = u''
    auth_user_48.email = u''
    auth_user_48.password = u'sha1$odEWIvBUG89Z$6c7f6891b946b8b12d72f5efb55bd33e66b65411'
    auth_user_48.is_staff = False
    auth_user_48.is_active = True
    auth_user_48.is_superuser = False
    auth_user_48.last_login = datetime.datetime(2012, 11, 2, 2, 27, 28, 626464, tzinfo=<UTC>)
    auth_user_48.date_joined = datetime.datetime(2012, 11, 2, 2, 27, 28, 626464, tzinfo=<UTC>)
    auth_user_48.save()

    auth_user_49 = User()
    auth_user_49.username = u'bev'
    auth_user_49.first_name = u''
    auth_user_49.last_name = u''
    auth_user_49.email = u''
    auth_user_49.password = u'sha1$ILMM1nT1JHL1$d1670405f5649c0c523a1410f363667d48803da5'
    auth_user_49.is_staff = False
    auth_user_49.is_active = True
    auth_user_49.is_superuser = False
    auth_user_49.last_login = datetime.datetime(2012, 11, 2, 2, 27, 28, 636410, tzinfo=<UTC>)
    auth_user_49.date_joined = datetime.datetime(2012, 11, 2, 2, 27, 28, 636410, tzinfo=<UTC>)
    auth_user_49.save()

    auth_user_50 = User()
    auth_user_50.username = u'daped'
    auth_user_50.first_name = u''
    auth_user_50.last_name = u''
    auth_user_50.email = u''
    auth_user_50.password = u'sha1$n5cWZnkTV0xt$9c9361d00cf1f6074f36f944496724c28d47ae6e'
    auth_user_50.is_staff = False
    auth_user_50.is_active = True
    auth_user_50.is_superuser = False
    auth_user_50.last_login = datetime.datetime(2012, 11, 2, 2, 36, 27, 513520, tzinfo=<UTC>)
    auth_user_50.date_joined = datetime.datetime(2012, 11, 2, 2, 27, 28, 191947, tzinfo=<UTC>)
    auth_user_50.save()

    auth_user_51 = User()
    auth_user_51.username = u'ilyakh'
    auth_user_51.first_name = u''
    auth_user_51.last_name = u''
    auth_user_51.email = u'ils.mailbox@gmail.com'
    auth_user_51.password = u'sha1$ShmcnTXYlkMz$289bfe558508971bd9effac0fcb56225c3c6d686'
    auth_user_51.is_staff = False
    auth_user_51.is_active = True
    auth_user_51.is_superuser = False
    auth_user_51.last_login = datetime.datetime(2012, 11, 2, 0, 10, 43, 522284, tzinfo=<UTC>)
    auth_user_51.date_joined = datetime.datetime(2012, 10, 31, 22, 53, 41, 432288, tzinfo=<UTC>)
    auth_user_51.save()

    from django.contrib.sessions.models import Session

    django_session_1 = Session()
    django_session_1.session_key = u'dac977707aeb67a88ae85faac9277d1c'
    django_session_1.session_data = u'YWIzYjg1MDdlOTFmNTIwZWM2NTJhY2Q1NGE1NmU1NzNmNTE0YTM5ZDqAAn1xAShVEHNvY2lhbHJl\nZzpvcGVuaWRxAmNzb2NpYWxyZWdpc3RyYXRpb24uY29udHJpYi5vcGVuaWQuY2xpZW50Ck9wZW5J\nRENsaWVudApxAymBcQR9cQUoVQhjb25zdW1lcnEGY29wZW5pZC5jb25zdW1lci5jb25zdW1lcgpD\nb25zdW1lcgpxBymBcQh9cQkoVQpfdG9rZW5fa2V5cQpVG19vcGVuaWRfY29uc3VtZXJfbGFzdF90\nb2tlblUHc2Vzc2lvbnELfXEMKGgCaAMpgXENfXEOKGgGaAcpgXEPfXEQKGgKVRtfb3BlbmlkX2Nv\nbnN1bWVyX2xhc3RfdG9rZW5xEWgLfXESKGgRY29wZW5pZC5jb25zdW1lci5kaXNjb3ZlcgpPcGVu\nSURTZXJ2aWNlRW5kcG9pbnQKcRMpgXEUfXEVKFUKY2xhaW1lZF9pZHEWTlUSZGlzcGxheV9pZGVu\ndGlmaWVycRdOVQpzZXJ2ZXJfdXJscRhVJWh0dHBzOi8vd3d3Lmdvb2dsZS5jb20vYWNjb3VudHMv\nbzgvdWRVC2Nhbm9uaWNhbElEcRlOVQhsb2NhbF9pZHEaTlUJdHlwZV91cmlzcRtdcRwoVSdodHRw\nOi8vc3BlY3Mub3BlbmlkLm5ldC9hdXRoLzIuMC9zZXJ2ZXJxHVUcaHR0cDovL29wZW5pZC5uZXQv\nc3J2L2F4LzEuMHEeVTRodHRwOi8vc3BlY3Mub3BlbmlkLm5ldC9leHRlbnNpb25zL3VpLzEuMC9t\nb2RlL3BvcHVwcR9VLmh0dHA6Ly9zcGVjcy5vcGVuaWQubmV0L2V4dGVuc2lvbnMvdWkvMS4wL2lj\nb25xIFUraHR0cDovL3NwZWNzLm9wZW5pZC5uZXQvZXh0ZW5zaW9ucy9wYXBlLzEuMHEhZVUKdXNl\nZF95YWRpc3EiiHViVSFfeWFkaXNfc2VydmljZXNfX29wZW5pZF9jb25zdW1lcl9xI2NvcGVuaWQu\neWFkaXMubWFuYWdlcgpZYWRpc1NlcnZpY2VNYW5hZ2VyCnEkKYFxJX1xJihVCHNlcnZpY2VzcSdd\nVQl5YWRpc191cmxxKFUlaHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS9hY2NvdW50cy9vOC9pZFUMc3Rh\ncnRpbmdfdXJscSlYJAAAAGh0dHA6Ly93d3cuZ29vZ2xlLmNvbS9hY2NvdW50cy9vOC9pZHEqVQtz\nZXNzaW9uX2tleXEraCNVCF9jdXJyZW50cSxoFHViVQRuZXh0VQQvbXkvcS11aAZjb3BlbmlkLmNv\nbnN1bWVyLmNvbnN1bWVyCkdlbmVyaWNDb25zdW1lcgpxLimBcS99cTAoVQpuZWdvdGlhdG9ycTFj\nb3BlbmlkLmFzc29jaWF0aW9uClNlc3Npb25OZWdvdGlhdG9yCnEyKYFxM31xNFUNYWxsb3dlZF90\neXBlc3E1XXE2KFUJSE1BQy1TSEExVQdESC1TSEExhnE3VQlITUFDLVNIQTFVDW5vLWVuY3J5cHRp\nb26GcThVC0hNQUMtU0hBMjU2VQlESC1TSEEyNTaGcTlVC0hNQUMtU0hBMjU2VQ1uby1lbmNyeXB0\naW9uhnE6ZXNiVQVzdG9yZXE7Y3NvY2lhbHJlZ2lzdHJhdGlvbi5jb250cmliLm9wZW5pZC5zdG9y\nYWdlCk9wZW5JRFN0b3JlCnE8KYFxPX1xPmJ1YnViVQxlbmRwb2ludF91cmxxP2gqaDtoPXViVQRu\nZXh0aC11aAZoLimBcUB9cUEoaDFoMimBcUJ9cUNoNV1xRChVCUhNQUMtU0hBMVUHREgtU0hBMYZx\nRVUJSE1BQy1TSEExVQ1uby1lbmNyeXB0aW9uhnFGVQtITUFDLVNIQTI1NlUJREgtU0hBMjU2hnFH\nVQtITUFDLVNIQTI1NlUNbm8tZW5jcnlwdGlvboZxSGVzYmg7aDwpgXFJfXFKYnVidWJoP1gkAAAA\naHR0cDovL3d3dy5nb29nbGUuY29tL2FjY291bnRzL284L2lkaDtoSXViVRFzb2NpYWxyZWc6dHdp\ndHRlcmNzb2NpYWxyZWdpc3RyYXRpb24uY29udHJpYi50d2l0dGVyLmNsaWVudApUd2l0dGVyCnFL\nKYFxTH1xTShVDl9yZXF1ZXN0X3Rva2VucU5jb2F1dGgyClRva2VuCnFPKYFxUH1xUShVBnNlY3Jl\ndHFSWCsAAAA4RFBlN3BLR0RtWDF2U0dtQjBYSGlLcEYwZFBod1k4OEJNUjhzekYzNjlJVQNrZXlx\nU1grAAAAeklJT2lYbFBoWkxIRUw4c0RUdklnNW5UckgzV2FvTVNpbzJOSHV1SHhYc3ViaAZjb2F1\ndGgyCkNvbnN1bWVyCnFUKYFxVX1xVihoUlUreDhaanJja2xNM00zWHh4cUl5RGJpdGdwUExrZEZE\nck82blk5NkxQdGFvc3FXaFNVFWVMQlo1RXl0TnBFNXZCb3RLS3o2Z3FYdWJ1YlUEbmV4dHFZaC11\nLg==\n'
    django_session_1.expire_date = datetime.datetime(2012, 11, 15, 18, 43, 57, 703244, tzinfo=<UTC>)
    django_session_1.save()

    django_session_2 = Session()
    django_session_2.session_key = u'bbe4b4352a5712188c110cc2e008c970'
    django_session_2.session_data = u'ZWQxYmJkN2ViYmI1YmU1YjExMjU0OGUxMzRmZDBkNjQ4M2VhNWM4YTqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQRNhgl1Lg==\n'
    django_session_2.expire_date = datetime.datetime(2012, 11, 16, 2, 36, 27, 521258, tzinfo=<UTC>)
    django_session_2.save()

    from django.contrib.sites.models import Site

    django_site_1 = Site()
    django_site_1.domain = u'127.0.0.1:8000'
    django_site_1.name = u'example.com'
    django_site_1.save()

    from django.contrib.admin.models import LogEntry


    from socialregistration.contrib.openid.models import OpenIDProfile

    openid_openidprofile_1 = OpenIDProfile()
    openid_openidprofile_1.user = auth_user_51
    openid_openidprofile_1.site = django_site_1
    openid_openidprofile_1.identity = u'https://www.google.com/accounts/o8/id?id=AItOawlWauOHceyGDJubssvJoAN3IrsXvdvsx80'
    openid_openidprofile_1.save()

    from socialregistration.contrib.openid.models import OpenIDStore

    openid_openidstore_1 = OpenIDStore()
    openid_openidstore_1.site = django_site_1
    openid_openidstore_1.server_url = u'https://www.google.com/accounts/o8/ud'
    openid_openidstore_1.handle = u'AMlYA9XxumYO25EeXp8UJRM5Gj2Yt2bloErzvY61Vk0_M-8V9aXbNVlQ'
    openid_openidstore_1.secret = u'DiP4DyNkW8q+GTraVDdDNnecikw=\n'
    openid_openidstore_1.issued = 1351719303
    openid_openidstore_1.lifetime = 1351719303
    openid_openidstore_1.assoc_type = u'HMAC-SHA1'
    openid_openidstore_1.save()

    from socialregistration.contrib.openid.models import OpenIDNonce

    openid_openidnonce_1 = OpenIDNonce()
    openid_openidnonce_1.server_url = u'https://www.google.com/accounts/o8/ud'
    openid_openidnonce_1.timestamp = 1351719374
    openid_openidnonce_1.salt = u'HVzBHF6OQPpp-w'
    openid_openidnonce_1.date_created = datetime.datetime(2012, 10, 31, 21, 36, 32, 597297, tzinfo=<UTC>)
    openid_openidnonce_1.save()

    openid_openidnonce_2 = OpenIDNonce()
    openid_openidnonce_2.server_url = u'https://www.google.com/accounts/o8/ud'
    openid_openidnonce_2.timestamp = 1351724003
    openid_openidnonce_2.salt = u'KtWes8eQeL3sGw'
    openid_openidnonce_2.date_created = datetime.datetime(2012, 10, 31, 22, 53, 41, 402952, tzinfo=<UTC>)
    openid_openidnonce_2.save()

    openid_openidnonce_3 = OpenIDNonce()
    openid_openidnonce_3.server_url = u'https://www.google.com/accounts/o8/ud'
    openid_openidnonce_3.timestamp = 1351724729
    openid_openidnonce_3.salt = u'1onW-jrjMXf8AA'
    openid_openidnonce_3.date_created = datetime.datetime(2012, 10, 31, 23, 5, 47, 595091, tzinfo=<UTC>)
    openid_openidnonce_3.save()

    openid_openidnonce_4 = OpenIDNonce()
    openid_openidnonce_4.server_url = u'https://www.google.com/accounts/o8/ud'
    openid_openidnonce_4.timestamp = 1351725627
    openid_openidnonce_4.salt = u'ROzUYfft1SFI5g'
    openid_openidnonce_4.date_created = datetime.datetime(2012, 10, 31, 23, 20, 45, 772498, tzinfo=<UTC>)
    openid_openidnonce_4.save()

    openid_openidnonce_5 = OpenIDNonce()
    openid_openidnonce_5.server_url = u'https://www.google.com/accounts/o8/ud'
    openid_openidnonce_5.timestamp = 1351725876
    openid_openidnonce_5.salt = u'wyMVIaM8l4I9oA'
    openid_openidnonce_5.date_created = datetime.datetime(2012, 10, 31, 23, 24, 54, 848516, tzinfo=<UTC>)
    openid_openidnonce_5.save()

    openid_openidnonce_6 = OpenIDNonce()
    openid_openidnonce_6.server_url = u'https://www.google.com/accounts/o8/ud'
    openid_openidnonce_6.timestamp = 1351731101
    openid_openidnonce_6.salt = u'lzLEg-iifTgjvQ'
    openid_openidnonce_6.date_created = datetime.datetime(2012, 11, 1, 0, 52, 0, 63696, tzinfo=<UTC>)
    openid_openidnonce_6.save()

    openid_openidnonce_7 = OpenIDNonce()
    openid_openidnonce_7.server_url = u'https://www.google.com/accounts/o8/ud'
    openid_openidnonce_7.timestamp = 1351732129
    openid_openidnonce_7.salt = u'FuPs7NTiXRdzjg'
    openid_openidnonce_7.date_created = datetime.datetime(2012, 11, 1, 1, 9, 8, 284872, tzinfo=<UTC>)
    openid_openidnonce_7.save()

    from socialregistration.contrib.twitter.models import TwitterProfile


    from socialregistration.contrib.twitter.models import TwitterRequestToken


    from socialregistration.contrib.twitter.models import TwitterAccessToken


    from socialregistration.contrib.github.models import GithubProfile


    from socialregistration.contrib.github.models import GithubAccessToken


    from djcelery.models import TaskMeta


    from djcelery.models import TaskSetMeta


    from djcelery.models import IntervalSchedule


    from djcelery.models import CrontabSchedule


    from djcelery.models import PeriodicTasks


    from djcelery.models import PeriodicTask


    from djcelery.models import WorkerState


    from djcelery.models import TaskState


    from kombu.transport.django.models import Queue


    from kombu.transport.django.models import Message


    from person.models import Person

    person_person_1 = Person()
    person_person_1.user = auth_user_51
    person_person_1.save()

    person_person_2 = Person()
    person_person_2.user = auth_user_1
    person_person_2.save()

    person_person_3 = Person()
    person_person_3.user = auth_user_50
    person_person_3.save()

    person_person_4 = Person()
    person_person_4.user = auth_user_2
    person_person_4.save()

    person_person_5 = Person()
    person_person_5.user = auth_user_3
    person_person_5.save()

    person_person_6 = Person()
    person_person_6.user = auth_user_4
    person_person_6.save()

    person_person_7 = Person()
    person_person_7.user = auth_user_5
    person_person_7.save()

    person_person_8 = Person()
    person_person_8.user = auth_user_6
    person_person_8.save()

    person_person_9 = Person()
    person_person_9.user = auth_user_7
    person_person_9.save()

    person_person_10 = Person()
    person_person_10.user = auth_user_8
    person_person_10.save()

    person_person_11 = Person()
    person_person_11.user = auth_user_9
    person_person_11.save()

    person_person_12 = Person()
    person_person_12.user = auth_user_10
    person_person_12.save()

    person_person_13 = Person()
    person_person_13.user = auth_user_11
    person_person_13.save()

    person_person_14 = Person()
    person_person_14.user = auth_user_12
    person_person_14.save()

    person_person_15 = Person()
    person_person_15.user = auth_user_13
    person_person_15.save()

    person_person_16 = Person()
    person_person_16.user = auth_user_14
    person_person_16.save()

    person_person_17 = Person()
    person_person_17.user = auth_user_15
    person_person_17.save()

    person_person_18 = Person()
    person_person_18.user = auth_user_16
    person_person_18.save()

    person_person_19 = Person()
    person_person_19.user = auth_user_17
    person_person_19.save()

    person_person_20 = Person()
    person_person_20.user = auth_user_18
    person_person_20.save()

    person_person_21 = Person()
    person_person_21.user = auth_user_19
    person_person_21.save()

    person_person_22 = Person()
    person_person_22.user = auth_user_20
    person_person_22.save()

    person_person_23 = Person()
    person_person_23.user = auth_user_21
    person_person_23.save()

    person_person_24 = Person()
    person_person_24.user = auth_user_22
    person_person_24.save()

    person_person_25 = Person()
    person_person_25.user = auth_user_23
    person_person_25.save()

    person_person_26 = Person()
    person_person_26.user = auth_user_24
    person_person_26.save()

    person_person_27 = Person()
    person_person_27.user = auth_user_25
    person_person_27.save()

    person_person_28 = Person()
    person_person_28.user = auth_user_26
    person_person_28.save()

    person_person_29 = Person()
    person_person_29.user = auth_user_27
    person_person_29.save()

    person_person_30 = Person()
    person_person_30.user = auth_user_28
    person_person_30.save()

    person_person_31 = Person()
    person_person_31.user = auth_user_29
    person_person_31.save()

    person_person_32 = Person()
    person_person_32.user = auth_user_30
    person_person_32.save()

    person_person_33 = Person()
    person_person_33.user = auth_user_31
    person_person_33.save()

    person_person_34 = Person()
    person_person_34.user = auth_user_32
    person_person_34.save()

    person_person_35 = Person()
    person_person_35.user = auth_user_33
    person_person_35.save()

    person_person_36 = Person()
    person_person_36.user = auth_user_34
    person_person_36.save()

    person_person_37 = Person()
    person_person_37.user = auth_user_35
    person_person_37.save()

    person_person_38 = Person()
    person_person_38.user = auth_user_36
    person_person_38.save()

    person_person_39 = Person()
    person_person_39.user = auth_user_37
    person_person_39.save()

    person_person_40 = Person()
    person_person_40.user = auth_user_38
    person_person_40.save()

    person_person_41 = Person()
    person_person_41.user = auth_user_39
    person_person_41.save()

    person_person_42 = Person()
    person_person_42.user = auth_user_40
    person_person_42.save()

    person_person_43 = Person()
    person_person_43.user = auth_user_41
    person_person_43.save()

    person_person_44 = Person()
    person_person_44.user = auth_user_42
    person_person_44.save()

    person_person_45 = Person()
    person_person_45.user = auth_user_43
    person_person_45.save()

    person_person_46 = Person()
    person_person_46.user = auth_user_44
    person_person_46.save()

    person_person_47 = Person()
    person_person_47.user = auth_user_45
    person_person_47.save()

    person_person_48 = Person()
    person_person_48.user = auth_user_46
    person_person_48.save()

    person_person_49 = Person()
    person_person_49.user = auth_user_47
    person_person_49.save()

    person_person_50 = Person()
    person_person_50.user = auth_user_48
    person_person_50.save()

    person_person_51 = Person()
    person_person_51.user = auth_user_49
    person_person_51.save()

    from group.models import Role


    from tag.models import Tag

    tag_tag_1 = Tag()
    tag_tag_1.name = u'circle'
    tag_tag_1.popularity = Decimal('0.00000')
    tag_tag_1.is_predefined = False
    tag_tag_1.save()

    tag_tag_2 = Tag()
    tag_tag_2.name = u'citizenship'
    tag_tag_2.popularity = Decimal('0.00000')
    tag_tag_2.is_predefined = False
    tag_tag_2.save()

    tag_tag_3 = Tag()
    tag_tag_3.name = u'energy'
    tag_tag_3.popularity = Decimal('0.00000')
    tag_tag_3.is_predefined = False
    tag_tag_3.save()

    tag_tag_4 = Tag()
    tag_tag_4.name = u'preface'
    tag_tag_4.popularity = Decimal('0.00000')
    tag_tag_4.is_predefined = False
    tag_tag_4.save()

    tag_tag_5 = Tag()
    tag_tag_5.name = u'tv'
    tag_tag_5.popularity = Decimal('0.00000')
    tag_tag_5.is_predefined = False
    tag_tag_5.save()

    from login.models import Attempt


    from login.models import Banned


    from communication.models import Message


    from person.models import Wish

    person_wish_1 = Wish()
    person_wish_1.created = datetime.datetime(2012, 11, 2, 2, 27, 28, 673147, tzinfo=<UTC>)
    person_wish_1.modified = datetime.datetime(2012, 11, 2, 2, 37, 18, 983911, tzinfo=<UTC>)
    person_wish_1.person = person_person_3
    person_wish_1.is_active = True
    person_wish_1.is_matched = False
    person_wish_1.expires = datetime.date(2013, 1, 31)
    person_wish_1.save()

    person_wish_1.tags.add(tag_tag_1)
    person_wish_1.tags.add(tag_tag_5)

    person_wish_2 = Wish()
    person_wish_2.created = datetime.datetime(2012, 11, 2, 2, 27, 28, 788146, tzinfo=<UTC>)
    person_wish_2.modified = datetime.datetime(2012, 11, 2, 2, 37, 18, 980454, tzinfo=<UTC>)
    person_wish_2.person = person_person_15
    person_wish_2.is_active = True
    person_wish_2.is_matched = False
    person_wish_2.expires = datetime.date(2013, 1, 31)
    person_wish_2.save()

    person_wish_2.tags.add(tag_tag_1)
    person_wish_2.tags.add(tag_tag_2)
    person_wish_2.tags.add(tag_tag_4)

    person_wish_3 = Wish()
    person_wish_3.created = datetime.datetime(2012, 11, 2, 2, 27, 28, 925053, tzinfo=<UTC>)
    person_wish_3.modified = datetime.datetime(2012, 11, 2, 2, 37, 18, 976835, tzinfo=<UTC>)
    person_wish_3.person = person_person_30
    person_wish_3.is_active = True
    person_wish_3.is_matched = False
    person_wish_3.expires = datetime.date(2013, 1, 31)
    person_wish_3.save()

    person_wish_3.tags.add(tag_tag_1)
    person_wish_3.tags.add(tag_tag_4)

    person_wish_4 = Wish()
    person_wish_4.created = datetime.datetime(2012, 11, 2, 2, 27, 29, 14763, tzinfo=<UTC>)
    person_wish_4.modified = datetime.datetime(2012, 11, 2, 2, 37, 18, 972924, tzinfo=<UTC>)
    person_wish_4.person = person_person_41
    person_wish_4.is_active = True
    person_wish_4.is_matched = False
    person_wish_4.expires = datetime.date(2013, 1, 31)
    person_wish_4.save()

    person_wish_4.tags.add(tag_tag_1)
    person_wish_4.tags.add(tag_tag_4)

    person_wish_5 = Wish()
    person_wish_5.created = datetime.datetime(2012, 11, 2, 2, 27, 28, 684814, tzinfo=<UTC>)
    person_wish_5.modified = datetime.datetime(2012, 11, 2, 2, 37, 18, 969494, tzinfo=<UTC>)
    person_wish_5.person = person_person_4
    person_wish_5.is_active = True
    person_wish_5.is_matched = False
    person_wish_5.expires = datetime.date(2013, 1, 31)
    person_wish_5.save()

    person_wish_5.tags.add(tag_tag_3)
    person_wish_5.tags.add(tag_tag_4)
    person_wish_5.tags.add(tag_tag_5)

    person_wish_6 = Wish()
    person_wish_6.created = datetime.datetime(2012, 11, 2, 2, 27, 28, 764897, tzinfo=<UTC>)
    person_wish_6.modified = datetime.datetime(2012, 11, 2, 2, 37, 18, 966205, tzinfo=<UTC>)
    person_wish_6.person = person_person_12
    person_wish_6.is_active = True
    person_wish_6.is_matched = False
    person_wish_6.expires = datetime.date(2013, 1, 31)
    person_wish_6.save()

    person_wish_6.tags.add(tag_tag_3)
    person_wish_6.tags.add(tag_tag_4)
    person_wish_6.tags.add(tag_tag_5)

    person_wish_7 = Wish()
    person_wish_7.created = datetime.datetime(2012, 11, 2, 2, 27, 28, 992652, tzinfo=<UTC>)
    person_wish_7.modified = datetime.datetime(2012, 11, 2, 2, 37, 18, 963071, tzinfo=<UTC>)
    person_wish_7.person = person_person_39
    person_wish_7.is_active = True
    person_wish_7.is_matched = False
    person_wish_7.expires = datetime.date(2013, 1, 31)
    person_wish_7.save()

    person_wish_7.tags.add(tag_tag_3)
    person_wish_7.tags.add(tag_tag_5)

    person_wish_8 = Wish()
    person_wish_8.created = datetime.datetime(2012, 11, 2, 2, 27, 28, 730169, tzinfo=<UTC>)
    person_wish_8.modified = datetime.datetime(2012, 11, 2, 2, 37, 18, 959372, tzinfo=<UTC>)
    person_wish_8.person = person_person_8
    person_wish_8.is_active = True
    person_wish_8.is_matched = False
    person_wish_8.expires = datetime.date(2013, 1, 31)
    person_wish_8.save()

    person_wish_8.tags.add(tag_tag_3)
    person_wish_8.tags.add(tag_tag_5)

    person_wish_9 = Wish()
    person_wish_9.created = datetime.datetime(2012, 11, 2, 2, 27, 28, 711472, tzinfo=<UTC>)
    person_wish_9.modified = datetime.datetime(2012, 11, 2, 2, 37, 18, 954817, tzinfo=<UTC>)
    person_wish_9.person = person_person_6
    person_wish_9.is_active = True
    person_wish_9.is_matched = False
    person_wish_9.expires = datetime.date(2013, 1, 31)
    person_wish_9.save()

    person_wish_9.tags.add(tag_tag_1)
    person_wish_9.tags.add(tag_tag_3)

    person_wish_10 = Wish()
    person_wish_10.created = datetime.datetime(2012, 11, 2, 2, 27, 29, 103173, tzinfo=<UTC>)
    person_wish_10.modified = datetime.datetime(2012, 11, 2, 2, 37, 18, 951236, tzinfo=<UTC>)
    person_wish_10.person = person_person_51
    person_wish_10.is_active = True
    person_wish_10.is_matched = False
    person_wish_10.expires = datetime.date(2013, 1, 31)
    person_wish_10.save()

    person_wish_10.tags.add(tag_tag_1)
    person_wish_10.tags.add(tag_tag_3)

    person_wish_11 = Wish()
    person_wish_11.created = datetime.datetime(2012, 11, 2, 2, 27, 28, 948556, tzinfo=<UTC>)
    person_wish_11.modified = datetime.datetime(2012, 11, 2, 2, 37, 18, 947638, tzinfo=<UTC>)
    person_wish_11.person = person_person_33
    person_wish_11.is_active = True
    person_wish_11.is_matched = False
    person_wish_11.expires = datetime.date(2013, 1, 31)
    person_wish_11.save()

    person_wish_11.tags.add(tag_tag_1)
    person_wish_11.tags.add(tag_tag_3)
    person_wish_11.tags.add(tag_tag_5)

    person_wish_12 = Wish()
    person_wish_12.created = datetime.datetime(2012, 11, 2, 2, 27, 28, 825731, tzinfo=<UTC>)
    person_wish_12.modified = datetime.datetime(2012, 11, 2, 2, 37, 18, 943760, tzinfo=<UTC>)
    person_wish_12.person = person_person_19
    person_wish_12.is_active = True
    person_wish_12.is_matched = False
    person_wish_12.expires = datetime.date(2013, 1, 31)
    person_wish_12.save()

    person_wish_12.tags.add(tag_tag_1)
    person_wish_12.tags.add(tag_tag_2)
    person_wish_12.tags.add(tag_tag_3)

    person_wish_13 = Wish()
    person_wish_13.created = datetime.datetime(2012, 11, 2, 2, 27, 29, 1784, tzinfo=<UTC>)
    person_wish_13.modified = datetime.datetime(2012, 11, 2, 2, 37, 18, 940015, tzinfo=<UTC>)
    person_wish_13.person = person_person_40
    person_wish_13.is_active = True
    person_wish_13.is_matched = False
    person_wish_13.expires = datetime.date(2013, 1, 31)
    person_wish_13.save()

    person_wish_13.tags.add(tag_tag_1)
    person_wish_13.tags.add(tag_tag_2)
    person_wish_13.tags.add(tag_tag_3)

    person_wish_14 = Wish()
    person_wish_14.created = datetime.datetime(2012, 11, 2, 2, 27, 29, 89589, tzinfo=<UTC>)
    person_wish_14.modified = datetime.datetime(2012, 11, 2, 2, 37, 18, 936333, tzinfo=<UTC>)
    person_wish_14.person = person_person_49
    person_wish_14.is_active = True
    person_wish_14.is_matched = False
    person_wish_14.expires = datetime.date(2013, 1, 31)
    person_wish_14.save()

    person_wish_14.tags.add(tag_tag_2)
    person_wish_14.tags.add(tag_tag_3)

    person_wish_15 = Wish()
    person_wish_15.created = datetime.datetime(2012, 11, 2, 2, 27, 29, 24293, tzinfo=<UTC>)
    person_wish_15.modified = datetime.datetime(2012, 11, 2, 2, 37, 18, 932220, tzinfo=<UTC>)
    person_wish_15.person = person_person_42
    person_wish_15.is_active = True
    person_wish_15.is_matched = False
    person_wish_15.expires = datetime.date(2013, 1, 31)
    person_wish_15.save()

    person_wish_15.tags.add(tag_tag_2)
    person_wish_15.tags.add(tag_tag_3)

    person_wish_16 = Wish()
    person_wish_16.created = datetime.datetime(2012, 11, 2, 2, 27, 28, 973736, tzinfo=<UTC>)
    person_wish_16.modified = datetime.datetime(2012, 11, 2, 2, 37, 18, 928746, tzinfo=<UTC>)
    person_wish_16.person = person_person_36
    person_wish_16.is_active = True
    person_wish_16.is_matched = False
    person_wish_16.expires = datetime.date(2013, 1, 31)
    person_wish_16.save()

    person_wish_16.tags.add(tag_tag_2)
    person_wish_16.tags.add(tag_tag_3)

    person_wish_17 = Wish()
    person_wish_17.created = datetime.datetime(2012, 11, 2, 2, 27, 28, 844074, tzinfo=<UTC>)
    person_wish_17.modified = datetime.datetime(2012, 11, 2, 2, 37, 18, 925542, tzinfo=<UTC>)
    person_wish_17.person = person_person_21
    person_wish_17.is_active = True
    person_wish_17.is_matched = False
    person_wish_17.expires = datetime.date(2013, 1, 31)
    person_wish_17.save()

    person_wish_17.tags.add(tag_tag_2)
    person_wish_17.tags.add(tag_tag_3)

    person_wish_18 = Wish()
    person_wish_18.created = datetime.datetime(2012, 11, 2, 2, 27, 28, 815268, tzinfo=<UTC>)
    person_wish_18.modified = datetime.datetime(2012, 11, 2, 2, 37, 18, 922371, tzinfo=<UTC>)
    person_wish_18.person = person_person_17
    person_wish_18.is_active = True
    person_wish_18.is_matched = False
    person_wish_18.expires = datetime.date(2013, 1, 31)
    person_wish_18.save()

    person_wish_18.tags.add(tag_tag_1)

    person_wish_19 = Wish()
    person_wish_19.created = datetime.datetime(2012, 11, 2, 2, 27, 28, 934260, tzinfo=<UTC>)
    person_wish_19.modified = datetime.datetime(2012, 11, 2, 2, 37, 18, 919304, tzinfo=<UTC>)
    person_wish_19.person = person_person_31
    person_wish_19.is_active = True
    person_wish_19.is_matched = False
    person_wish_19.expires = datetime.date(2013, 1, 31)
    person_wish_19.save()

    person_wish_19.tags.add(tag_tag_1)

    person_wish_20 = Wish()
    person_wish_20.created = datetime.datetime(2012, 11, 2, 2, 27, 28, 872997, tzinfo=<UTC>)
    person_wish_20.modified = datetime.datetime(2012, 11, 2, 2, 37, 18, 915379, tzinfo=<UTC>)
    person_wish_20.person = person_person_24
    person_wish_20.is_active = True
    person_wish_20.is_matched = False
    person_wish_20.expires = datetime.date(2013, 1, 31)
    person_wish_20.save()

    person_wish_20.tags.add(tag_tag_1)

    person_wish_21 = Wish()
    person_wish_21.created = datetime.datetime(2012, 11, 2, 2, 27, 28, 698562, tzinfo=<UTC>)
    person_wish_21.modified = datetime.datetime(2012, 11, 2, 2, 37, 18, 912129, tzinfo=<UTC>)
    person_wish_21.person = person_person_5
    person_wish_21.is_active = True
    person_wish_21.is_matched = False
    person_wish_21.expires = datetime.date(2013, 1, 31)
    person_wish_21.save()

    person_wish_21.tags.add(tag_tag_1)
    person_wish_21.tags.add(tag_tag_4)
    person_wish_21.tags.add(tag_tag_5)

    person_wish_22 = Wish()
    person_wish_22.created = datetime.datetime(2012, 11, 2, 2, 27, 28, 744010, tzinfo=<UTC>)
    person_wish_22.modified = datetime.datetime(2012, 11, 2, 2, 37, 18, 908097, tzinfo=<UTC>)
    person_wish_22.person = person_person_10
    person_wish_22.is_active = True
    person_wish_22.is_matched = False
    person_wish_22.expires = datetime.date(2013, 1, 31)
    person_wish_22.save()

    person_wish_22.tags.add(tag_tag_1)
    person_wish_22.tags.add(tag_tag_4)
    person_wish_22.tags.add(tag_tag_5)

    person_wish_23 = Wish()
    person_wish_23.created = datetime.datetime(2012, 11, 2, 2, 27, 28, 738977, tzinfo=<UTC>)
    person_wish_23.modified = datetime.datetime(2012, 11, 2, 2, 37, 18, 904470, tzinfo=<UTC>)
    person_wish_23.person = person_person_9
    person_wish_23.is_active = True
    person_wish_23.is_matched = False
    person_wish_23.expires = datetime.date(2013, 1, 31)
    person_wish_23.save()

    person_wish_23.tags.add(tag_tag_4)

    person_wish_24 = Wish()
    person_wish_24.created = datetime.datetime(2012, 11, 2, 2, 27, 28, 759820, tzinfo=<UTC>)
    person_wish_24.modified = datetime.datetime(2012, 11, 2, 2, 37, 18, 900935, tzinfo=<UTC>)
    person_wish_24.person = person_person_11
    person_wish_24.is_active = True
    person_wish_24.is_matched = False
    person_wish_24.expires = datetime.date(2013, 1, 31)
    person_wish_24.save()

    person_wish_24.tags.add(tag_tag_4)

    person_wish_25 = Wish()
    person_wish_25.created = datetime.datetime(2012, 11, 2, 2, 27, 28, 859159, tzinfo=<UTC>)
    person_wish_25.modified = datetime.datetime(2012, 11, 2, 2, 37, 18, 898023, tzinfo=<UTC>)
    person_wish_25.person = person_person_23
    person_wish_25.is_active = True
    person_wish_25.is_matched = False
    person_wish_25.expires = datetime.date(2013, 1, 31)
    person_wish_25.save()

    person_wish_25.tags.add(tag_tag_1)
    person_wish_25.tags.add(tag_tag_2)
    person_wish_25.tags.add(tag_tag_5)

    person_wish_26 = Wish()
    person_wish_26.created = datetime.datetime(2012, 11, 2, 2, 27, 29, 67369, tzinfo=<UTC>)
    person_wish_26.modified = datetime.datetime(2012, 11, 2, 2, 37, 18, 894516, tzinfo=<UTC>)
    person_wish_26.person = person_person_47
    person_wish_26.is_active = True
    person_wish_26.is_matched = False
    person_wish_26.expires = datetime.date(2013, 1, 31)
    person_wish_26.save()

    person_wish_26.tags.add(tag_tag_1)
    person_wish_26.tags.add(tag_tag_2)
    person_wish_26.tags.add(tag_tag_5)

    person_wish_27 = Wish()
    person_wish_27.created = datetime.datetime(2012, 11, 2, 2, 27, 28, 878243, tzinfo=<UTC>)
    person_wish_27.modified = datetime.datetime(2012, 11, 2, 2, 37, 18, 890946, tzinfo=<UTC>)
    person_wish_27.person = person_person_25
    person_wish_27.is_active = True
    person_wish_27.is_matched = False
    person_wish_27.expires = datetime.date(2013, 1, 31)
    person_wish_27.save()

    person_wish_27.tags.add(tag_tag_1)
    person_wish_27.tags.add(tag_tag_2)
    person_wish_27.tags.add(tag_tag_5)

    person_wish_28 = Wish()
    person_wish_28.created = datetime.datetime(2012, 11, 2, 2, 27, 28, 892284, tzinfo=<UTC>)
    person_wish_28.modified = datetime.datetime(2012, 11, 2, 2, 37, 18, 886876, tzinfo=<UTC>)
    person_wish_28.person = person_person_26
    person_wish_28.is_active = True
    person_wish_28.is_matched = False
    person_wish_28.expires = datetime.date(2013, 1, 31)
    person_wish_28.save()

    person_wish_28.tags.add(tag_tag_2)
    person_wish_28.tags.add(tag_tag_5)

    person_wish_29 = Wish()
    person_wish_29.created = datetime.datetime(2012, 11, 2, 2, 27, 28, 906396, tzinfo=<UTC>)
    person_wish_29.modified = datetime.datetime(2012, 11, 2, 2, 37, 18, 883506, tzinfo=<UTC>)
    person_wish_29.person = person_person_28
    person_wish_29.is_active = True
    person_wish_29.is_matched = False
    person_wish_29.expires = datetime.date(2013, 1, 31)
    person_wish_29.save()

    person_wish_29.tags.add(tag_tag_1)
    person_wish_29.tags.add(tag_tag_2)
    person_wish_29.tags.add(tag_tag_5)

    person_wish_30 = Wish()
    person_wish_30.created = datetime.datetime(2012, 11, 2, 2, 27, 29, 42890, tzinfo=<UTC>)
    person_wish_30.modified = datetime.datetime(2012, 11, 2, 2, 37, 18, 880374, tzinfo=<UTC>)
    person_wish_30.person = person_person_44
    person_wish_30.is_active = True
    person_wish_30.is_matched = False
    person_wish_30.expires = datetime.date(2013, 1, 31)
    person_wish_30.save()

    person_wish_30.tags.add(tag_tag_3)
    person_wish_30.tags.add(tag_tag_4)

    person_wish_31 = Wish()
    person_wish_31.created = datetime.datetime(2012, 11, 2, 2, 27, 29, 80531, tzinfo=<UTC>)
    person_wish_31.modified = datetime.datetime(2012, 11, 2, 2, 37, 18, 876482, tzinfo=<UTC>)
    person_wish_31.person = person_person_48
    person_wish_31.is_active = True
    person_wish_31.is_matched = False
    person_wish_31.expires = datetime.date(2013, 1, 31)
    person_wish_31.save()

    person_wish_31.tags.add(tag_tag_3)
    person_wish_31.tags.add(tag_tag_4)

    person_wish_32 = Wish()
    person_wish_32.created = datetime.datetime(2012, 11, 2, 2, 27, 28, 801427, tzinfo=<UTC>)
    person_wish_32.modified = datetime.datetime(2012, 11, 2, 2, 37, 18, 872385, tzinfo=<UTC>)
    person_wish_32.person = person_person_16
    person_wish_32.is_active = True
    person_wish_32.is_matched = False
    person_wish_32.expires = datetime.date(2013, 1, 31)
    person_wish_32.save()

    person_wish_32.tags.add(tag_tag_2)
    person_wish_32.tags.add(tag_tag_3)
    person_wish_32.tags.add(tag_tag_4)

    person_wish_33 = Wish()
    person_wish_33.created = datetime.datetime(2012, 11, 2, 2, 27, 28, 645137, tzinfo=<UTC>)
    person_wish_33.modified = datetime.datetime(2012, 11, 2, 2, 37, 18, 868337, tzinfo=<UTC>)
    person_wish_33.person = person_person_1
    person_wish_33.is_active = True
    person_wish_33.is_matched = False
    person_wish_33.expires = datetime.date(2013, 1, 31)
    person_wish_33.save()

    person_wish_33.tags.add(tag_tag_2)
    person_wish_33.tags.add(tag_tag_3)
    person_wish_33.tags.add(tag_tag_4)

    person_wish_34 = Wish()
    person_wish_34.created = datetime.datetime(2012, 11, 2, 2, 27, 29, 52350, tzinfo=<UTC>)
    person_wish_34.modified = datetime.datetime(2012, 11, 2, 2, 37, 18, 863946, tzinfo=<UTC>)
    person_wish_34.person = person_person_45
    person_wish_34.is_active = True
    person_wish_34.is_matched = False
    person_wish_34.expires = datetime.date(2013, 1, 31)
    person_wish_34.save()

    person_wish_34.tags.add(tag_tag_3)
    person_wish_34.tags.add(tag_tag_4)

    person_wish_35 = Wish()
    person_wish_35.created = datetime.datetime(2012, 11, 2, 2, 27, 29, 98219, tzinfo=<UTC>)
    person_wish_35.modified = datetime.datetime(2012, 11, 2, 2, 37, 18, 859672, tzinfo=<UTC>)
    person_wish_35.person = person_person_50
    person_wish_35.is_active = True
    person_wish_35.is_matched = False
    person_wish_35.expires = datetime.date(2013, 1, 31)
    person_wish_35.save()

    person_wish_35.tags.add(tag_tag_5)

    person_wish_36 = Wish()
    person_wish_36.created = datetime.datetime(2012, 11, 2, 2, 27, 28, 783000, tzinfo=<UTC>)
    person_wish_36.modified = datetime.datetime(2012, 11, 2, 2, 37, 18, 856072, tzinfo=<UTC>)
    person_wish_36.person = person_person_14
    person_wish_36.is_active = True
    person_wish_36.is_matched = False
    person_wish_36.expires = datetime.date(2013, 1, 31)
    person_wish_36.save()

    person_wish_36.tags.add(tag_tag_5)

    person_wish_37 = Wish()
    person_wish_37.created = datetime.datetime(2012, 11, 2, 2, 27, 28, 901188, tzinfo=<UTC>)
    person_wish_37.modified = datetime.datetime(2012, 11, 2, 2, 37, 18, 851491, tzinfo=<UTC>)
    person_wish_37.person = person_person_27
    person_wish_37.is_active = True
    person_wish_37.is_matched = False
    person_wish_37.expires = datetime.date(2013, 1, 31)
    person_wish_37.save()

    person_wish_37.tags.add(tag_tag_5)

    person_wish_38 = Wish()
    person_wish_38.created = datetime.datetime(2012, 11, 2, 2, 27, 28, 920011, tzinfo=<UTC>)
    person_wish_38.modified = datetime.datetime(2012, 11, 2, 2, 37, 18, 848231, tzinfo=<UTC>)
    person_wish_38.person = person_person_29
    person_wish_38.is_active = True
    person_wish_38.is_matched = False
    person_wish_38.expires = datetime.date(2013, 1, 31)
    person_wish_38.save()

    person_wish_38.tags.add(tag_tag_5)

    person_wish_39 = Wish()
    person_wish_39.created = datetime.datetime(2012, 11, 2, 2, 27, 28, 939805, tzinfo=<UTC>)
    person_wish_39.modified = datetime.datetime(2012, 11, 2, 2, 37, 18, 845310, tzinfo=<UTC>)
    person_wish_39.person = person_person_32
    person_wish_39.is_active = True
    person_wish_39.is_matched = False
    person_wish_39.expires = datetime.date(2013, 1, 31)
    person_wish_39.save()

    person_wish_39.tags.add(tag_tag_4)
    person_wish_39.tags.add(tag_tag_5)

    person_wish_40 = Wish()
    person_wish_40.created = datetime.datetime(2012, 11, 2, 2, 27, 29, 33746, tzinfo=<UTC>)
    person_wish_40.modified = datetime.datetime(2012, 11, 2, 2, 37, 18, 842228, tzinfo=<UTC>)
    person_wish_40.person = person_person_43
    person_wish_40.is_active = True
    person_wish_40.is_matched = False
    person_wish_40.expires = datetime.date(2013, 1, 31)
    person_wish_40.save()

    person_wish_40.tags.add(tag_tag_4)
    person_wish_40.tags.add(tag_tag_5)

    person_wish_41 = Wish()
    person_wish_41.created = datetime.datetime(2012, 11, 2, 2, 27, 28, 963160, tzinfo=<UTC>)
    person_wish_41.modified = datetime.datetime(2012, 11, 2, 2, 37, 18, 837601, tzinfo=<UTC>)
    person_wish_41.person = person_person_34
    person_wish_41.is_active = True
    person_wish_41.is_matched = False
    person_wish_41.expires = datetime.date(2013, 1, 31)
    person_wish_41.save()

    person_wish_41.tags.add(tag_tag_3)

    person_wish_42 = Wish()
    person_wish_42.created = datetime.datetime(2012, 11, 2, 2, 27, 28, 987516, tzinfo=<UTC>)
    person_wish_42.modified = datetime.datetime(2012, 11, 2, 2, 37, 18, 833699, tzinfo=<UTC>)
    person_wish_42.person = person_person_38
    person_wish_42.is_active = True
    person_wish_42.is_matched = False
    person_wish_42.expires = datetime.date(2013, 1, 31)
    person_wish_42.save()

    person_wish_42.tags.add(tag_tag_3)

    person_wish_43 = Wish()
    person_wish_43.created = datetime.datetime(2012, 11, 2, 2, 27, 29, 61429, tzinfo=<UTC>)
    person_wish_43.modified = datetime.datetime(2012, 11, 2, 2, 37, 18, 830281, tzinfo=<UTC>)
    person_wish_43.person = person_person_46
    person_wish_43.is_active = True
    person_wish_43.is_matched = False
    person_wish_43.expires = datetime.date(2013, 1, 31)
    person_wish_43.save()

    person_wish_43.tags.add(tag_tag_3)

    person_wish_44 = Wish()
    person_wish_44.created = datetime.datetime(2012, 11, 2, 2, 27, 28, 724222, tzinfo=<UTC>)
    person_wish_44.modified = datetime.datetime(2012, 11, 2, 2, 37, 18, 827134, tzinfo=<UTC>)
    person_wish_44.person = person_person_7
    person_wish_44.is_active = True
    person_wish_44.is_matched = False
    person_wish_44.expires = datetime.date(2013, 1, 31)
    person_wish_44.save()

    person_wish_44.tags.add(tag_tag_3)

    person_wish_45 = Wish()
    person_wish_45.created = datetime.datetime(2012, 11, 2, 2, 27, 28, 968710, tzinfo=<UTC>)
    person_wish_45.modified = datetime.datetime(2012, 11, 2, 2, 37, 18, 824043, tzinfo=<UTC>)
    person_wish_45.person = person_person_35
    person_wish_45.is_active = True
    person_wish_45.is_matched = False
    person_wish_45.expires = datetime.date(2013, 1, 31)
    person_wish_45.save()

    person_wish_45.tags.add(tag_tag_3)

    person_wish_46 = Wish()
    person_wish_46.created = datetime.datetime(2012, 11, 2, 2, 27, 28, 777934, tzinfo=<UTC>)
    person_wish_46.modified = datetime.datetime(2012, 11, 2, 2, 37, 18, 820973, tzinfo=<UTC>)
    person_wish_46.person = person_person_13
    person_wish_46.is_active = True
    person_wish_46.is_matched = False
    person_wish_46.expires = datetime.date(2013, 1, 31)
    person_wish_46.save()

    person_wish_46.tags.add(tag_tag_3)

    person_wish_47 = Wish()
    person_wish_47.created = datetime.datetime(2012, 11, 2, 2, 27, 28, 667266, tzinfo=<UTC>)
    person_wish_47.modified = datetime.datetime(2012, 11, 2, 2, 37, 18, 817809, tzinfo=<UTC>)
    person_wish_47.person = person_person_2
    person_wish_47.is_active = True
    person_wish_47.is_matched = False
    person_wish_47.expires = datetime.date(2013, 1, 31)
    person_wish_47.save()

    person_wish_47.tags.add(tag_tag_2)

    person_wish_48 = Wish()
    person_wish_48.created = datetime.datetime(2012, 11, 2, 2, 27, 28, 852973, tzinfo=<UTC>)
    person_wish_48.modified = datetime.datetime(2012, 11, 2, 2, 37, 18, 814754, tzinfo=<UTC>)
    person_wish_48.person = person_person_22
    person_wish_48.is_active = True
    person_wish_48.is_matched = False
    person_wish_48.expires = datetime.date(2013, 1, 31)
    person_wish_48.save()

    person_wish_48.tags.add(tag_tag_2)

    person_wish_49 = Wish()
    person_wish_49.created = datetime.datetime(2012, 11, 2, 2, 27, 28, 820481, tzinfo=<UTC>)
    person_wish_49.modified = datetime.datetime(2012, 11, 2, 2, 37, 18, 811387, tzinfo=<UTC>)
    person_wish_49.person = person_person_18
    person_wish_49.is_active = True
    person_wish_49.is_matched = False
    person_wish_49.expires = datetime.date(2013, 1, 31)
    person_wish_49.save()

    person_wish_49.tags.add(tag_tag_2)

    person_wish_50 = Wish()
    person_wish_50.created = datetime.datetime(2012, 11, 2, 2, 27, 28, 839024, tzinfo=<UTC>)
    person_wish_50.modified = datetime.datetime(2012, 11, 2, 2, 37, 18, 808300, tzinfo=<UTC>)
    person_wish_50.person = person_person_20
    person_wish_50.is_active = True
    person_wish_50.is_matched = False
    person_wish_50.expires = datetime.date(2013, 1, 31)
    person_wish_50.save()

    person_wish_50.tags.add(tag_tag_2)

    person_wish_51 = Wish()
    person_wish_51.created = datetime.datetime(2012, 11, 2, 2, 27, 28, 982624, tzinfo=<UTC>)
    person_wish_51.modified = datetime.datetime(2012, 11, 2, 2, 37, 18, 804987, tzinfo=<UTC>)
    person_wish_51.person = person_person_37
    person_wish_51.is_active = True
    person_wish_51.is_matched = False
    person_wish_51.expires = datetime.date(2013, 1, 31)
    person_wish_51.save()

    person_wish_51.tags.add(tag_tag_2)

    from group.models import Slot


    from group.models import Group


