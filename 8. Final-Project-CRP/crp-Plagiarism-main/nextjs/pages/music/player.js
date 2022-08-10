import { useState, useEffect } from "react";
import Player from "../../components/music/Player";

function PlayerPage() {
  const [songs] = useState([
    {
      title: "Fly Away",
      artist: "The Fat Rat",
      img_src: "/images/Flyaway.jpg",
      src: "/music/FlyAway.mp3",
    },
    {
      title: "A whole New World",
      artist: "ZAYN",
      img_src: "/images/aladdin.jpg",
      src: "/music/Aladdin.mp3",
    },
    {
      title: "Shallow",
      artist: "Lady Gaga & Bradely",
      img_src: "/images/shallow.jpg",
      src: "/music/Shallow.mp3",
    },
    {
      title: "Faded",
      artist: "Alan Walker",
      img_src: "/images/Faded.jpg",
      src: "/music/Faded.mp3",
    },
    {
      title: "Danza Kuduro",
      artist: "Don Omar",
      img_src: "/images/DanzaKuduro.jpg",
      src: "/music/DanzaKuduro.mp3",
    }
  ]);

  const [currentSongIndex, setCurrentSongIndex] = useState(0);
  const [nextSongIndex, setNextSongIndex] = useState(0);

  useEffect(() => {
    setNextSongIndex(() => {
      if (currentSongIndex + 1 > songs.length - 1) {
        return 0;
      } else {
        return currentSongIndex + 1;
      }
    });
  }, [currentSongIndex, songs.length]);

  return ( <div className= "PlayerPage" >
    <div className="App">
      <Player
        currentSongIndex={currentSongIndex}
        setCurrentSongIndex={setCurrentSongIndex}
        nextSongIndex={nextSongIndex}
        songs={songs}
      />
    </div>
    </div>
  );
}

export default PlayerPage;
