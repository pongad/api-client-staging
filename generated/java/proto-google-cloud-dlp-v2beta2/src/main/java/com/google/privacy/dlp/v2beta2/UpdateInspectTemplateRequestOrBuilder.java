// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: google/privacy/dlp/v2beta2/dlp.proto

package com.google.privacy.dlp.v2beta2;

public interface UpdateInspectTemplateRequestOrBuilder extends
    // @@protoc_insertion_point(interface_extends:google.privacy.dlp.v2beta2.UpdateInspectTemplateRequest)
    com.google.protobuf.MessageOrBuilder {

  /**
   * <pre>
   * Resource name of organization and inspectTemplate to be updated, for
   * example `organizations/433245324/inspectTemplates/432452342`.
   * </pre>
   *
   * <code>string name = 1;</code>
   */
  java.lang.String getName();
  /**
   * <pre>
   * Resource name of organization and inspectTemplate to be updated, for
   * example `organizations/433245324/inspectTemplates/432452342`.
   * </pre>
   *
   * <code>string name = 1;</code>
   */
  com.google.protobuf.ByteString
      getNameBytes();

  /**
   * <pre>
   * New InspectTemplate value.
   * </pre>
   *
   * <code>.google.privacy.dlp.v2beta2.InspectTemplate inspect_template = 2;</code>
   */
  boolean hasInspectTemplate();
  /**
   * <pre>
   * New InspectTemplate value.
   * </pre>
   *
   * <code>.google.privacy.dlp.v2beta2.InspectTemplate inspect_template = 2;</code>
   */
  com.google.privacy.dlp.v2beta2.InspectTemplate getInspectTemplate();
  /**
   * <pre>
   * New InspectTemplate value.
   * </pre>
   *
   * <code>.google.privacy.dlp.v2beta2.InspectTemplate inspect_template = 2;</code>
   */
  com.google.privacy.dlp.v2beta2.InspectTemplateOrBuilder getInspectTemplateOrBuilder();

  /**
   * <pre>
   * Mask to control which fields get updated.
   * </pre>
   *
   * <code>.google.protobuf.FieldMask update_mask = 3;</code>
   */
  boolean hasUpdateMask();
  /**
   * <pre>
   * Mask to control which fields get updated.
   * </pre>
   *
   * <code>.google.protobuf.FieldMask update_mask = 3;</code>
   */
  com.google.protobuf.FieldMask getUpdateMask();
  /**
   * <pre>
   * Mask to control which fields get updated.
   * </pre>
   *
   * <code>.google.protobuf.FieldMask update_mask = 3;</code>
   */
  com.google.protobuf.FieldMaskOrBuilder getUpdateMaskOrBuilder();
}