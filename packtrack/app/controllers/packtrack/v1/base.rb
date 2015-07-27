require "grape-swagger"

module Packtrack
  module V1
    class Base < Grape::API
      mount Packtrack::V1::Users
      # mount API::V1::AnotherResource

      add_swagger_documentation(
        api_version: "v1",
        hide_documentation_path: true,
        mount_path: "/packtrack/v1/swagger_doc",
        hide_format: true
      )
    end
  end
end
