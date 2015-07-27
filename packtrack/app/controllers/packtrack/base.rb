module Packtrack
  class Base < Grape::API
    mount Packtrack::V1::Base
  end
end
