import {
  Streamlit,
  ComponentProps,
  withStreamlitConnection
} from "streamlit-component-lib"
import React, { Component } from "react"

import ReactPlayer from "react-player"
import HeightObserver from "./height-observer"

interface ComponentState {
  playerEvents: any;
  isPlaying: boolean;
}
class StreamlitPlayer extends Component<ComponentProps, ComponentState> {
  player: any;

  constructor(props: ComponentProps) {
    super(props);
    this.player = React.createRef()
    this.state = {
      playerEvents: {},
      isPlaying: false
    }
  }

  componentDidMount() {
      let events: any = {}

      this.props.args.events.forEach((name: string) => {
        events[name] = (data?: any) => {
          Streamlit.setComponentValue({
            name: name,
            data: data
          })
        }
      })

      this.setState({ playerEvents: events })
  }

  render() {
    const {
      url,
      height,
      playing,
      loop,
      controls,
      light,
      volume,
      muted,
      playbackRate,
      progressInterval,
      playInline,
      config,
      time,
    } = this.props.args

    const { playerEvents } = this.state

    if (this.player.current !== null && this.player.current !== undefined) {
      console.log(this.player.current)
      console.log(this.player.current !== null)
      this.player.current.seekTo(time)
      console.log(`seek ${time}`)
    }

    return (
      <HeightObserver onChange={Streamlit.setFrameHeight} fixedHeight={height}>
      <ReactPlayer
        ref={this.player}
        // youtubeConfig={{
        //   playerVars: {
        //     start: 33
        //   }
        // }}
        url={url}
        width="100%"
        height={height || undefined}
        playing={playing || undefined}
        loop={loop || undefined}
        controls={controls || undefined}
        light={light || undefined}
        volume={volume}
        muted={muted || undefined}
        playbackRate={playbackRate}
        progressInterval={progressInterval}
        playsinline={playInline || undefined}
        config={config || undefined}
        {...playerEvents}
        />
    </HeightObserver>
    )
  }
}

const WrappedStreamlitPlayer = withStreamlitConnection(StreamlitPlayer)

export { StreamlitPlayer, WrappedStreamlitPlayer }