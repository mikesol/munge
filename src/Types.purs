module Munge.Types where

type Cruft =
  { args :: { name :: String }
  , cat :: String
  , name :: String
  , ph :: String
  , pid :: Int
  , tid :: Int
  , ts :: Int
  }

type MoreCruft =
  { args :: {}
  , cat :: String
  , dur :: Int
  , name :: String
  , ph :: String
  , pid :: Int
  , tdur :: Int
  , tid :: Int
  , ts :: Int
  , tts :: Int
  }