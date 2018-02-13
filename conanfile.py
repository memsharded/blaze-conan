from conans import ConanFile, tools
import os

class BlazeConan(ConanFile):
   name = "blaze"
   version = "3.3"
   # No settings/options are necessary, this is header only

   def source(self):
      self.run("git clone https://bitbucket.org/blaze-lib/blaze")
      self.run("cd blaze && git checkout v%s" % self.version)

   def package(self):
      self.copy("*.h", src="blaze", dst="include")
