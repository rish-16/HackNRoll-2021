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
  playing: boolean;
}
class StreamlitPlayer extends Component<ComponentProps, ComponentState> {
  player: any;



  constructor(props: ComponentProps) {
    super(props);
    this.player = React.createRef()
    this.state = {
      playerEvents: {},
      playing: false
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

  getRangeContainingTime = (time: number) => {
    const { ranges } = this.props.args
    ranges.forEach((range: any) => {
      // if time is in range
      if (time >= range.start && time <= range.end)
        return range

      if (time < range.start)
        return null
      
    })
    return null
  }

  getNextRangeForTime = (time: number) => {
    const { ranges } = this.props.args
    for (let i = 0; i < ranges.length; i++) {
      let currRange = ranges[i]
      // if already in a range
      if (time >= currRange.start && time <= currRange.end)
        return null
      
      // use the first range which has a start larger than time
      if (time < currRange.start)
        return currRange
    }
    return null
  }

  // onProgress({ playedSeconds }: { playedSeconds: number }) {
  onProgress = ({ playedSeconds }: { playedSeconds: number }) => {
    if (this.player?.current === null || this.player?.current === undefined)
      return 

    console.log('onProgress')
    // if (playedSeconds < 30) {
    //   this.player.current.seekTo(30)
    //   this.setState({ playing: true })
    // }
    let nextRange = this.getNextRangeForTime(playedSeconds)
    if (nextRange !== null) {
      this.player.current.seekTo(nextRange.start)
      this.setState({ playing: true })
    }

  }

  render() {
    const {
      url,
      height,
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

      const { playerEvents, playing } = this.state

    if (this.player.current !== null && this.player.current !== undefined) {
      // console.log(this.player.current)
      // console.log(this.player.current !== null)
      // this.player.current.seekTo(time)
      // console.log(`seek ${time}`)
    }
    

    return (
      <>
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
        // playing={playing || undefined}
        playing={playing}
        loop={loop || undefined}
        controls={controls || undefined}
        light={light || undefined}
        volume={volume}
        muted={muted || undefined}
        playbackRate={playbackRate}
        // progressInterval={progressInterval}
        progressInterval={200}
        playsinline={playInline || undefined}
        config={config || undefined}
        {...playerEvents}
        onProgress={this.onProgress}
        />
    </HeightObserver>

    </>
    )
  }
}

const WrappedStreamlitPlayer = withStreamlitConnection(StreamlitPlayer)

export { StreamlitPlayer, WrappedStreamlitPlayer }