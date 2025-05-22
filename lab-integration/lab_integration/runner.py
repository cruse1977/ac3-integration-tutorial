#!/usr/bin/env python

from collections.abc import Iterable
from netboxlabs.diode.sdk.ingester import Entity
from worker.backend import Backend
from worker.models import Metadata, Policy


class LabIntegration(Backend):

    def setup(self) -> Metadata:
        return Metadata(name="lab_integration", app_name="lab_integration_app", app_version="1.0.0")

    def run(self, policy_name: str, policy: Policy) -> Iterable[Entity]:
        
        entities = []

        return entities