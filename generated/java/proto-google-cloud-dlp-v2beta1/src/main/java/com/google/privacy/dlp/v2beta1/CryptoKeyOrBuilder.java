// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: google/privacy/dlp/v2beta1/dlp.proto

package com.google.privacy.dlp.v2beta1;

public interface CryptoKeyOrBuilder extends
    // @@protoc_insertion_point(interface_extends:google.privacy.dlp.v2beta1.CryptoKey)
    com.google.protobuf.MessageOrBuilder {

  /**
   * <code>.google.privacy.dlp.v2beta1.TransientCryptoKey transient = 1;</code>
   */
  com.google.privacy.dlp.v2beta1.TransientCryptoKey getTransient();
  /**
   * <code>.google.privacy.dlp.v2beta1.TransientCryptoKey transient = 1;</code>
   */
  com.google.privacy.dlp.v2beta1.TransientCryptoKeyOrBuilder getTransientOrBuilder();

  /**
   * <code>.google.privacy.dlp.v2beta1.UnwrappedCryptoKey unwrapped = 2;</code>
   */
  com.google.privacy.dlp.v2beta1.UnwrappedCryptoKey getUnwrapped();
  /**
   * <code>.google.privacy.dlp.v2beta1.UnwrappedCryptoKey unwrapped = 2;</code>
   */
  com.google.privacy.dlp.v2beta1.UnwrappedCryptoKeyOrBuilder getUnwrappedOrBuilder();

  /**
   * <code>.google.privacy.dlp.v2beta1.KmsWrappedCryptoKey kms_wrapped = 3;</code>
   */
  com.google.privacy.dlp.v2beta1.KmsWrappedCryptoKey getKmsWrapped();
  /**
   * <code>.google.privacy.dlp.v2beta1.KmsWrappedCryptoKey kms_wrapped = 3;</code>
   */
  com.google.privacy.dlp.v2beta1.KmsWrappedCryptoKeyOrBuilder getKmsWrappedOrBuilder();

  public com.google.privacy.dlp.v2beta1.CryptoKey.SourceCase getSourceCase();
}