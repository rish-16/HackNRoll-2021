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
          controls: true
        }}
        width={200}
        disabled={false}
    /> */}
  </React.StrictMode>,
  document.getElementById("root")
)
