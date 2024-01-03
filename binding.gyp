{
  "targets": [
    {
      "target_name": "addon",
      "sources": [ "addon.cpp" ],
      "cflags!": [ "-fno-exceptions" ],
      "cflags_cc!": [ "-fno-exceptions" ],
      "configurations": [
        {
          "target_defaults": {
            "cflags": [ "-fno-exceptions" ],
            "cflags_cc": [ "-fno-exceptions" ]
          },
          "defines": [ "NAPI_CPP_EXCEPTIONS" ]
        }
      ]
    }
  ]
}
