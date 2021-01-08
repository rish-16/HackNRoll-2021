import React from "react"
import ReactDOM from "react-dom"
import { StreamlitPlayer, WrappedStreamlitPlayer } from "./streamlit-player"

ReactDOM.render(
  <React.StrictMode>
    {/* run for Streamlit */}
    <WrappedStreamlitPlayer/>

    {/* run for development */}
    {/* <StreamlitPlayer
        args={{
          url: 'https://www.youtube.com/watch?v=-DP1i2ZU9gk',
          events: [],
          controls: true,
          ranges: [
            {start: 0.79, end: 4.73
            },
            {start: 58.21, end: 62.77
            },
            {start: 80.28, end: 91.0
            },
            {start: 102.12, end: 106.92
            },
            {start: 110.73, end: 114.58
            },
            {start: 133.1, end: 137.69
            },
            {start: 137.69, end: 141.32
            },
            {start: 147.62, end: 149.74
            },
            {start: 149.74, end: 153.519
            },
            {start: 160.544, end: 164.87
            },
            {start: 174.29, end: 183.98
            },
            {start: 207.81, end: 211.79
            },
            {start: 261.149, end: 264.58
            },
            {start: 307.73, end: 309.93
            },
            {start: 313.5, end: 316.337
            },
            {start: 318.42, end: 323.26
            },
            {start: 329.03, end: 334.28
            },
            {start: 358.93, end: 364.34
            },
            {start: 400.7, end: 405.23
            },
            {start: 503.3, end: 520.3090000000001
            },
            {start: 556.056, end: 561.8639999999999
            },
            {start: 633.55, end: 637.8399999999999
            },
            {start: 667.4, end: 672.052
            },
            {start: 694.46, end: 697.1700000000001
            },
            {start: 722.21, end: 726.74
            },
            {start: 736.58, end: 739.47
            },
            {start: 741.82, end: 747.0
            },
            {start: 820.91, end: 824.1
            },
            {start: 824.1, end: 830.52
            },
            {start: 841.38, end: 846.36
            },
            {start: 875.74, end: 879.64
            },
            {start: 1011.871, end: 1020.81
            },
            {start: 1020.81, end: 1027.839
            },
            {start: 1032.99, end: 1037.589
            },
            {start: 1037.589, end: 1043.52
            },
            {start: 1060.597, end: 1064.01
            },
            {start: 1201.8, end: 1208.81
            },
            {start: 1259.45, end: 1265.21
            },
            {start: 1334.74, end: 1339.63
            },
            {start: 1431.11, end: 1434.83
            },
            {start: 1434.83, end: 1437.9199999999998
            },
            {start: 1472.32, end: 1474.56
            },
            {start: 1477.06, end: 1483.49
            },
            {start: 1490.32, end: 1492.63
            },
            {start: 1500.41, end: 1514.74
            },
            {start: 1514.74, end: 1518.124
            },
            {start: 1535.59, end: 1542.91
            },
            {start: 1616.59, end: 1625.16
            },
            {start: 1682.08, end: 1684.99
            },
            {start: 1711.0, end: 1719.65
            },
            {start: 1782.17, end: 1787.77
            },
            {start: 1850.78, end: 1860.29
            },
            {start: 1860.29, end: 1867.93
            },
            {start: 2000.454, end: 2006.36
            },
            {start: 2008.55, end: 2011.74
            },
            {start: 2034.256, end: 2038.4
            },
            {start: 2060.81, end: 2064.02
            },
            {start: 2103.25, end: 2126.566
            },
            {start: 2138.18, end: 2142.41
            },
            {start: 2227.14, end: 2237.96
            },
            {start: 2300.94, end: 2308.87
            },
            {start: 2308.87, end: 2311.6
            },
            {start: 2330.55, end: 2334.73
            },
            {start: 2337.962, end: 2339.92
            },
            {start: 2410.72, end: 2427.43
            },
            {start: 2427.43, end: 2436.85
            },
            {start: 2443.35, end: 2457.56
            },
            {start: 2466.24, end: 2473.03
            }
          ]
        }}
        width={200}
        disabled={false}
    /> */}
  </React.StrictMode>,
  document.getElementById("root")
)
