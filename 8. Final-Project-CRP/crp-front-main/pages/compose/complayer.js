import { useState, useEffect } from "react";
import ComPlayer from "../../components/compose/ComPlayer";

function ComPlayerPage() {
  const [songs] = useState([
    {
      title: "MuseGAN",
      artist: "GAN",
      img_src: "/images/musegan.jpg",
      src: "/music/musegan.mp3",
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

  return ( <div className= "Player1Page" >
    <div className="App">
      <ComPlayer
        currentSongIndex={currentSongIndex}
        setCurrentSongIndex={setCurrentSongIndex}
        nextSongIndex={nextSongIndex}
        songs={songs}
      />
    </div>
    </div>
  );
}

export default ComPlayerPage;
