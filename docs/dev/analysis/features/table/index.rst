
Table
=====

A table is composed of rows of cells. An implicit sequence of *grid columns*
align cells across rows. If there are no merged cells, the grid columns
correspond directly to the visual columns.

All table content is contained in its cells.

In addition to this overview, there are the following more specialized
feature analyses:

.. toctree::
   :titlesonly:

   table-props
   table-row
   table-cell
   cell-merge


Specimen XML
------------

.. highlight:: xml

The following XML is generated by Word when inserting a 2x2 table::

    <w:tbl>
      <w:tblPr>
        <w:tblStyle w:val="TableGrid"/>
        <w:tblW w:type="auto" w:w="0"/>
        <w:tblLook w:firstColumn="1" w:firstRow="1" w:lastColumn="0"
                   w:lastRow="0" w:noHBand="0" w:noVBand="1" w:val="04A0"/>
      </w:tblPr>
      <w:tblGrid>
        <w:gridCol w:w="4788"/>
        <w:gridCol w:w="4788"/>
      </w:tblGrid>
      <w:tr>
        <w:tc/>
          <w:tcPr>
            <w:tcW w:type="dxa" w:w="4788"/>
          </w:tcPr>
          <w:p/>
        </w:tc>
        <w:tc>
          <w:tcPr>
            <w:tcW w:type="dxa" w:w="4788"/>
          </w:tcPr>
          <w:p/>
        </w:tc>
      </w:tr>
      <w:tr>
        <w:tc>
          <w:tcPr>
            <w:tcW w:type="dxa" w:w="4788"/>
          </w:tcPr>
          <w:p/>
        </w:tc>
        <w:tc>
          <w:tcPr>
            <w:tcW w:type="dxa" w:w="4788"/>
          </w:tcPr>
          <w:p/>
        </w:tc>
      </w:tr>
    </w:tbl>


Schema Definitions
------------------

.. highlight:: xml

::

  <xsd:complexType name="CT_Tbl">  <!-- denormalized -->
    <xsd:sequence>
      <xsd:group    ref="EG_RangeMarkupElements"        minOccurs="0" maxOccurs="unbounded"/>
      <xsd:element name="tblPr"       type="CT_TblPr"/>
      <xsd:element name="tblGrid"     type="CT_TblGrid"/>
      <xsd:choice                                       minOccurs="0" maxOccurs="unbounded">
        <xsd:element name="tr"        type="CT_Row"/>
        <xsd:element name="customXml" type="CT_CustomXmlRow"/>
        <xsd:element name="sdt"       type="CT_SdtRow"/>
        <xsd:group    ref="EG_RunLevelElts"             minOccurs="0" maxOccurs="unbounded"/>
      </xsd:choice>
    </xsd:sequence>
  </xsd:complexType>

  <xsd:complexType name="CT_TblPr">  <!-- denormalized -->
    <xsd:sequence>
      <xsd:element name="tblStyle"            type="CT_String"        minOccurs="0"/>
      <xsd:element name="tblpPr"              type="CT_TblPPr"        minOccurs="0"/>
      <xsd:element name="tblOverlap"          type="CT_TblOverlap"    minOccurs="0"/>
      <xsd:element name="bidiVisual"          type="CT_OnOff"         minOccurs="0"/>
      <xsd:element name="tblStyleRowBandSize" type="CT_DecimalNumber" minOccurs="0"/>
      <xsd:element name="tblStyleColBandSize" type="CT_DecimalNumber" minOccurs="0"/>
      <xsd:element name="tblW"                type="CT_TblWidth"      minOccurs="0"/>
      <xsd:element name="jc"                  type="CT_JcTable"       minOccurs="0"/>
      <xsd:element name="tblCellSpacing"      type="CT_TblWidth"      minOccurs="0"/>
      <xsd:element name="tblInd"              type="CT_TblWidth"      minOccurs="0"/>
      <xsd:element name="tblBorders"          type="CT_TblBorders"    minOccurs="0"/>
      <xsd:element name="shd"                 type="CT_Shd"           minOccurs="0"/>
      <xsd:element name="tblLayout"           type="CT_TblLayoutType" minOccurs="0"/>
      <xsd:element name="tblCellMar"          type="CT_TblCellMar"    minOccurs="0"/>
      <xsd:element name="tblLook"             type="CT_TblLook"       minOccurs="0"/>
      <xsd:element name="tblCaption"          type="CT_String"        minOccurs="0"/>
      <xsd:element name="tblDescription"      type="CT_String"        minOccurs="0"/>
      <xsd:element name="tblPrChange"         type="CT_TblPrChange"   minOccurs="0"/>
    </xsd:sequence>

  <xsd:complexType name="CT_TblGrid">  <!-- denormalized -->
    <xsd:sequence>
      <xsd:element name="gridCol"       type="CT_TblGridCol"    minOccurs="0" maxOccurs="unbounded"/>
      <xsd:element name="tblGridChange" type="CT_TblGridChange" minOccurs="0"/>
    </xsd:sequence>
  </xsd:complexType>

  <xsd:complexType name="CT_TblGridCol">
    <xsd:attribute name="w" type="s:ST_TwipsMeasure"/>
  </xsd:complexType>

  <xsd:complexType name="CT_Row">
    <xsd:sequence>
      <xsd:element name="tblPrEx" type="CT_TblPrEx" minOccurs="0"/>
      <xsd:element name="trPr"    type="CT_TrPr"    minOccurs="0"/>
      <xsd:group   ref="EG_ContentCellContent"      minOccurs="0" maxOccurs="unbounded"/>
    </xsd:sequence>
    <xsd:attribute name="rsidRPr" type="ST_LongHexNumber"/>
    <xsd:attribute name="rsidR"   type="ST_LongHexNumber"/>
    <xsd:attribute name="rsidDel" type="ST_LongHexNumber"/>
    <xsd:attribute name="rsidTr"  type="ST_LongHexNumber"/>
  </xsd:complexType>

  <!-- component types --------------------------------- -->

  <xsd:group name="EG_ContentCellContent">
    <xsd:choice>
      <xsd:element name="tc"        type="CT_Tc"            minOccurs="0" maxOccurs="unbounded"/>
      <xsd:element name="customXml" type="CT_CustomXmlCell"/>
      <xsd:element name="sdt"       type="CT_SdtCell"/>
      <xsd:group   ref="EG_RunLevelElts"                    minOccurs="0" maxOccurs="unbounded"/>
    </xsd:choice>
  </xsd:group>

  <xsd:group name="EG_RunLevelElts">  <!-- denormalized -->
    <xsd:choice>
      <xsd:element name="proofErr"                    type="CT_ProofErr"/>
      <xsd:element name="permStart"                   type="CT_PermStart"/>
      <xsd:element name="permEnd"                     type="CT_Perm"/>
      <xsd:element name="ins"                         type="CT_RunTrackChange"/>
      <xsd:element name="del"                         type="CT_RunTrackChange"/>
      <xsd:element name="moveFrom"                    type="CT_RunTrackChange"/>
      <xsd:element name="moveTo"                      type="CT_RunTrackChange"/>
      <xsd:element  ref="m:oMathPara"                 type="CT_OMathPara"/>
      <xsd:element  ref="m:oMath"                     type="CT_OMath"/>
      <xsd:element name="bookmarkStart"               type="CT_Bookmark"/>
      <xsd:element name="bookmarkEnd"                 type="CT_MarkupRange"/>
      <xsd:element name="moveFromRangeStart"          type="CT_MoveBookmark"/>
      <xsd:element name="moveFromRangeEnd"            type="CT_MarkupRange"/>
      <xsd:element name="moveToRangeStart"            type="CT_MoveBookmark"/>
      <xsd:element name="moveToRangeEnd"              type="CT_MarkupRange"/>
      <xsd:element name="commentRangeStart"           type="CT_MarkupRange"/>
      <xsd:element name="commentRangeEnd"             type="CT_MarkupRange"/>
      <xsd:element name="customXmlInsRangeStart"      type="CT_TrackChange"/>
      <xsd:element name="customXmlInsRangeEnd"        type="CT_Markup"/>
      <xsd:element name="customXmlDelRangeStart"      type="CT_TrackChange"/>
      <xsd:element name="customXmlDelRangeEnd"        type="CT_Markup"/>
      <xsd:element name="customXmlMoveFromRangeStart" type="CT_TrackChange"/>
      <xsd:element name="customXmlMoveFromRangeEnd"   type="CT_Markup"/>
      <xsd:element name="customXmlMoveToRangeStart"   type="CT_TrackChange"/>
      <xsd:element name="customXmlMoveToRangeEnd"     type="CT_Markup"/>
    </xsd:choice>
  </xsd:group>

  <xsd:group name="EG_RangeMarkupElements">
    <xsd:choice>
      <xsd:element name="bookmarkStart"               type="CT_Bookmark"/>
      <xsd:element name="bookmarkEnd"                 type="CT_MarkupRange"/>
      <xsd:element name="moveFromRangeStart"          type="CT_MoveBookmark"/>
      <xsd:element name="moveFromRangeEnd"            type="CT_MarkupRange"/>
      <xsd:element name="moveToRangeStart"            type="CT_MoveBookmark"/>
      <xsd:element name="moveToRangeEnd"              type="CT_MarkupRange"/>
      <xsd:element name="commentRangeStart"           type="CT_MarkupRange"/>
      <xsd:element name="commentRangeEnd"             type="CT_MarkupRange"/>
      <xsd:element name="customXmlInsRangeStart"      type="CT_TrackChange"/>
      <xsd:element name="customXmlInsRangeEnd"        type="CT_Markup"/>
      <xsd:element name="customXmlDelRangeStart"      type="CT_TrackChange"/>
      <xsd:element name="customXmlDelRangeEnd"        type="CT_Markup"/>
      <xsd:element name="customXmlMoveFromRangeStart" type="CT_TrackChange"/>
      <xsd:element name="customXmlMoveFromRangeEnd"   type="CT_Markup"/>
      <xsd:element name="customXmlMoveToRangeStart"   type="CT_TrackChange"/>
      <xsd:element name="customXmlMoveToRangeEnd"     type="CT_Markup"/>
    </xsd:choice>
  </xsd:group>

  <xsd:simpleType name="ST_TwipsMeasure">
    <xsd:union memberTypes="ST_UnsignedDecimalNumber ST_PositiveUniversalMeasure"/>
  </xsd:simpleType>

  <xsd:simpleType name="ST_UnsignedDecimalNumber">
    <xsd:restriction base="xsd:unsignedLong"/>
  </xsd:simpleType>

  <xsd:simpleType name="ST_PositiveUniversalMeasure">
    <xsd:restriction base="ST_UniversalMeasure">
      <xsd:pattern value="[0-9]+(\.[0-9]+)?(mm|cm|in|pt|pc|pi)"/>
    </xsd:restriction>
  </xsd:simpleType>
