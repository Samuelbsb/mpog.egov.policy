# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import mpog.egov.policy


class MpogEgovPolicyLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=mpog.egov.policy)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'mpog.egov.policy:default')


MPOG_EGOV_POLICY_FIXTURE = MpogEgovPolicyLayer()


MPOG_EGOV_POLICY_INTEGRATION_TESTING = IntegrationTesting(
    bases=(MPOG_EGOV_POLICY_FIXTURE,),
    name='MpogEgovPolicyLayer:IntegrationTesting'
)


MPOG_EGOV_POLICY_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(MPOG_EGOV_POLICY_FIXTURE,),
    name='MpogEgovPolicyLayer:FunctionalTesting'
)


MPOG_EGOV_POLICY_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        MPOG_EGOV_POLICY_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='MpogEgovPolicyLayer:AcceptanceTesting'
)
