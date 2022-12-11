# encoding: utf-8

from docxxx.api import Document  # noqa

__version__ = "0.8.11"


# register custom Part classes with opc package reader

from docxxx.opc.constants import CONTENT_TYPE as CT, RELATIONSHIP_TYPE as RT
from docxxx.opc.part import PartFactory
from docxxx.opc.parts.coreprops import CorePropertiesPart

from docxxx.parts.document import DocumentPart
from docxxx.parts.hdrftr import FooterPart, HeaderPart
from docxxx.parts.image import ImagePart
from docxxx.parts.numbering import NumberingPart
from docxxx.parts.settings import SettingsPart
from docxxx.parts.styles import StylesPart


def part_class_selector(content_type, reltype):
    if reltype == RT.IMAGE:
        return ImagePart
    return None


PartFactory.part_class_selector = part_class_selector
PartFactory.part_type_for[CT.OPC_CORE_PROPERTIES] = CorePropertiesPart
PartFactory.part_type_for[CT.WML_DOCUMENT_MAIN] = DocumentPart
PartFactory.part_type_for[CT.WML_FOOTER] = FooterPart
PartFactory.part_type_for[CT.WML_HEADER] = HeaderPart
PartFactory.part_type_for[CT.WML_NUMBERING] = NumberingPart
PartFactory.part_type_for[CT.WML_SETTINGS] = SettingsPart
PartFactory.part_type_for[CT.WML_STYLES] = StylesPart

del (
    CT,
    CorePropertiesPart,
    DocumentPart,
    FooterPart,
    HeaderPart,
    NumberingPart,
    PartFactory,
    SettingsPart,
    StylesPart,
    part_class_selector,
)
