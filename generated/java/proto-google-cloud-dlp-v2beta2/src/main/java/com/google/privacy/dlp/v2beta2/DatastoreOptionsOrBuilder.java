// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: google/privacy/dlp/v2beta2/storage.proto

package com.google.privacy.dlp.v2beta2;

public interface DatastoreOptionsOrBuilder extends
    // @@protoc_insertion_point(interface_extends:google.privacy.dlp.v2beta2.DatastoreOptions)
    com.google.protobuf.MessageOrBuilder {

  /**
   * <pre>
   * A partition ID identifies a grouping of entities. The grouping is always
   * by project and namespace, however the namespace ID may be empty.
   * </pre>
   *
   * <code>.google.privacy.dlp.v2beta2.PartitionId partition_id = 1;</code>
   */
  boolean hasPartitionId();
  /**
   * <pre>
   * A partition ID identifies a grouping of entities. The grouping is always
   * by project and namespace, however the namespace ID may be empty.
   * </pre>
   *
   * <code>.google.privacy.dlp.v2beta2.PartitionId partition_id = 1;</code>
   */
  com.google.privacy.dlp.v2beta2.PartitionId getPartitionId();
  /**
   * <pre>
   * A partition ID identifies a grouping of entities. The grouping is always
   * by project and namespace, however the namespace ID may be empty.
   * </pre>
   *
   * <code>.google.privacy.dlp.v2beta2.PartitionId partition_id = 1;</code>
   */
  com.google.privacy.dlp.v2beta2.PartitionIdOrBuilder getPartitionIdOrBuilder();

  /**
   * <pre>
   * The kind to process.
   * </pre>
   *
   * <code>.google.privacy.dlp.v2beta2.KindExpression kind = 2;</code>
   */
  boolean hasKind();
  /**
   * <pre>
   * The kind to process.
   * </pre>
   *
   * <code>.google.privacy.dlp.v2beta2.KindExpression kind = 2;</code>
   */
  com.google.privacy.dlp.v2beta2.KindExpression getKind();
  /**
   * <pre>
   * The kind to process.
   * </pre>
   *
   * <code>.google.privacy.dlp.v2beta2.KindExpression kind = 2;</code>
   */
  com.google.privacy.dlp.v2beta2.KindExpressionOrBuilder getKindOrBuilder();
}
