window.BENCHMARK_DATA = {
  "lastUpdate": 1607958629723,
  "repoUrl": "https://github.com/dmarar/opentelemetry-python",
  "entries": {
    "OpenTelemetry Python Benchmarks - Python 3.9 -": [
      {
        "commit": {
          "author": {
            "email": "55284676+dmarar@users.noreply.github.com",
            "name": "Dilip M",
            "username": "dmarar"
          },
          "committer": {
            "email": "55284676+dmarar@users.noreply.github.com",
            "name": "Dilip M",
            "username": "dmarar"
          },
          "distinct": true,
          "id": "a59a217f3e79dddcc57268da2d1a7d1cbe3a8f22",
          "message": "Merge branch 'master' of https://github.com/open-telemetry/opentelemetry-python",
          "timestamp": "2020-12-14T20:36:56+05:30",
          "tree_id": "0988f882c87f2990a11c1c6e4dec0779347c53c7",
          "url": "https://github.com/dmarar/opentelemetry-python/commit/a59a217f3e79dddcc57268da2d1a7d1cbe3a8f22"
        },
        "date": 1607958593147,
        "tool": "pytest",
        "benches": [
          {
            "name": "opentelemetry-sdk/tests/performance/benchmarks/trace/test_benchmark_trace.py::test_simple_start_span",
            "value": 31344.969205366164,
            "unit": "iter/sec",
            "range": "stddev: 0.000004547287717004292",
            "extra": "mean: 31.90304617778355 usec\nrounds: 4461"
          },
          {
            "name": "opentelemetry-sdk/tests/performance/benchmarks/trace/test_benchmark_trace.py::test_simple_start_as_current_span",
            "value": 24620.85901751475,
            "unit": "iter/sec",
            "range": "stddev: 0.000006272343371650499",
            "extra": "mean: 40.61596710694055 usec\nrounds: 7722"
          }
        ]
      }
    ],
    "OpenTelemetry Python Benchmarks - Python 3.8 -": [
      {
        "commit": {
          "author": {
            "email": "55284676+dmarar@users.noreply.github.com",
            "name": "Dilip M",
            "username": "dmarar"
          },
          "committer": {
            "email": "55284676+dmarar@users.noreply.github.com",
            "name": "Dilip M",
            "username": "dmarar"
          },
          "distinct": true,
          "id": "a59a217f3e79dddcc57268da2d1a7d1cbe3a8f22",
          "message": "Merge branch 'master' of https://github.com/open-telemetry/opentelemetry-python",
          "timestamp": "2020-12-14T20:36:56+05:30",
          "tree_id": "0988f882c87f2990a11c1c6e4dec0779347c53c7",
          "url": "https://github.com/dmarar/opentelemetry-python/commit/a59a217f3e79dddcc57268da2d1a7d1cbe3a8f22"
        },
        "date": 1607958628710,
        "tool": "pytest",
        "benches": [
          {
            "name": "opentelemetry-sdk/tests/performance/benchmarks/trace/test_benchmark_trace.py::test_simple_start_span",
            "value": 22973.62935961229,
            "unit": "iter/sec",
            "range": "stddev: 0.000040928124448248146",
            "extra": "mean: 43.52816807247718 usec\nrounds: 4742"
          },
          {
            "name": "opentelemetry-sdk/tests/performance/benchmarks/trace/test_benchmark_trace.py::test_simple_start_as_current_span",
            "value": 16486.594144189745,
            "unit": "iter/sec",
            "range": "stddev: 0.00010284949566608537",
            "extra": "mean: 60.65534162205497 usec\nrounds: 8606"
          }
        ]
      }
    ]
  }
}