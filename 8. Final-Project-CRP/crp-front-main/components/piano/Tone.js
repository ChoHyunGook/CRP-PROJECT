import * as Tone from "tone"

 const playC4 =(keycode) =>{
    const synth = new Tone.Synth().toDestination();
    synth.triggerAttackRelease("C4","8n");
    return keycode
    }

 const playDb4 = (keycode) =>{
    const synth = new Tone.Synth().toDestination();
    synth.triggerAttackRelease("Db4","8n");
    return keycode
    }
    
 const playD4 = (keycode) =>{
    const synth = new Tone.Synth().toDestination();
    synth.triggerAttackRelease("D4","8n");
    return keycode
    }   
    
    const playEb4 = (keycode) =>{
    const synth = new Tone.Synth().toDestination();
    synth.triggerAttackRelease("Eb4","8n");
    return keycode
    }   

    const playE4 = (keycode) =>{
    const synth = new Tone.Synth().toDestination();
    synth.triggerAttackRelease("E4","8n");
    return keycode
    }
    
    const playF4 = (keycode) =>{
    const synth = new Tone.Synth().toDestination();
    synth.triggerAttackRelease("F4","8n");
    return keycode
    }
        
    const playGb4 = (keycode) =>{
    const synth = new Tone.Synth().toDestination();
    synth.triggerAttackRelease("Gb4","8n");
    return keycode
    }
    
    const playG4 = (keycode) =>{
    const synth = new Tone.Synth().toDestination();
    synth.triggerAttackRelease("G4","8n");
    return keycode
   } 
    
   const playAb4 = (keycode) =>{
    const synth = new Tone.Synth().toDestination();
    synth.triggerAttackRelease("Ab4","8n");
    return keycode
    }
    
    const playA4 = (keycode) =>{
    const synth = new Tone.Synth().toDestination();
    synth.triggerAttackRelease("A4","8n");
    return keycode
    }

    const playBb4 = (keycode) =>{
    const synth = new Tone.Synth().toDestination();
    synth.triggerAttackRelease("Bb4","8n");
    return keycode
    }
        
    const playB4 = (keycode) =>{
    const synth = new Tone.Synth().toDestination();
    synth.triggerAttackRelease("B4","8n");
    return keycode
    }

    const playC5 = (keycode) =>{
    const synth = new Tone.Synth().toDestination();
    synth.triggerAttackRelease("C5","8n");
    return keycode
    }
    
    const playDb5 = (keycode) =>{
    const synth = new Tone.Synth().toDestination();
    synth.triggerAttackRelease("Db5","8n");
    return keycode
    }
    
    const playD5 = (keycode) =>{
    const synth = new Tone.Synth().toDestination();
    synth.triggerAttackRelease("D5","8n");
    return keycode
    }
        
    const playEb5 = (keycode) =>{
    const synth = new Tone.Synth().toDestination();
    synth.triggerAttackRelease("Eb5","8n");
    return keycode
    }

    const playE5 = (keycode) =>{
    const synth = new Tone.Synth().toDestination();
    synth.triggerAttackRelease("E5","8n");
    return keycode
    }

    const playF5 = (keycode) =>{
     const synth = new Tone.Synth().toDestination();
     synth.triggerAttackRelease("F5","8n");
     return keycode
    }

    const playGb5 = (keycode) =>{
    const synth = new Tone.Synth().toDestination();
    synth.triggerAttackRelease("Gb5","8n");
    return keycode
    }

    const playG5 = (keycode) =>{
    const synth = new Tone.Synth().toDestination();
    synth.triggerAttackRelease("G5","8n");
    return keycode
    }

    const playAb5 = (keycode) =>{
    const synth = new Tone.Synth().toDestination();
    synth.triggerAttackRelease("Ab5","8n");
    return keycode
    }

    const playA5 = (keycode) =>{
    const synth = new Tone.Synth().toDestination();
     synth.triggerAttackRelease("A5","8n");
     return keycode
    }

    const playBb5 = (keycode) =>{
    const synth = new Tone.Synth().toDestination();
    synth.triggerAttackRelease("Bb5","8n");
    return keycode
    }

    const playB5 = (keycode) =>{
    const synth = new Tone.Synth().toDestination();
    synth.triggerAttackRelease("B5","8n");
    return keycode
    }

    const playC6 = (keycode) =>{
    const synth = new Tone.Synth().toDestination();
    synth.triggerAttackRelease("C6","8n");
    return keycode
    }

 const PlayNote = (event) =>{

    if(event.keyCode ===65){
        
        let a = localStorage.getItem("note")
        let b =  playC4("A");
        let c = a + ','+b
        //alert('최종 저장된 값: '+ c)
        localStorage.setItem("note", c)

    }

    if(event.keyCode ===87){

        let a = localStorage.getItem("note")
        let b =  playDb4("W");
        let c = a + ','+b
        //alert('최종 저장된 값: '+ c)
        localStorage.setItem("note", c)

    }

    if(event.keyCode ===83){
        let a = localStorage.getItem("note")
        let b =  playD4("S");
        let c = a + ','+b
        //alert('최종 저장된 값: '+ c)
        localStorage.setItem("note", c)
    }
    if(event.keyCode ===69){
        let a = localStorage.getItem("note")
        let b =  playEb4("E");
        let c = a + ','+b
        //alert('최종 저장된 값: '+ c)
        localStorage.setItem("note", c)
    }
    if(event.keyCode ===68){
        let a = localStorage.getItem("note")
        let b =  playE4("D");
        let c = a + ','+b
        //alert('최종 저장된 값: '+ c)
        localStorage.setItem("note", c)
    }
    if(event.keyCode ===70){
        let a = localStorage.getItem("note")
        let b =  playF4("F");
        let c = a + ','+b
        //alert('최종 저장된 값: '+ c)
        localStorage.setItem("note", c)
    }
    if(event.keyCode ===84){
        let a = localStorage.getItem("note")
        let b =  playGb4("T");
        let c = a + ','+b
        //alert('최종 저장된 값: '+ c)
        localStorage.setItem("note", c)
    }
    if(event.keyCode ===71){
        let a = localStorage.getItem("note")
        let b =  playG4("G");
        let c = a + ','+b
        //alert('최종 저장된 값: '+ c)
        localStorage.setItem("note", c)
    }
    if(event.keyCode ===89){
        let a = localStorage.getItem("note")
        let b =  playAb4("Y");
        let c = a + ','+b
        //alert('최종 저장된 값: '+ c)
        localStorage.setItem("note", c)
    }
    if(event.keyCode ===72){
        let a = localStorage.getItem("note")
        let b =  playA4("H");
        let c = a + ','+b
        //alert('최종 저장된 값: '+ c)
        localStorage.setItem("note", c)
    }
    if(event.keyCode ===85){
        let a = localStorage.getItem("note")
        let b =  playBb4("U");
        let c = a + ','+b
        //alert('최종 저장된 값: '+ c)
        localStorage.setItem("note", c)
    }
    if(event.keyCode ===74){
        let a = localStorage.getItem("note")
        let b =  playB4("J");
        let c = a + ','+b
        //alert('최종 저장된 값: '+ c)
        localStorage.setItem("note", c)
    }

    if(event.keyCode ===75){
        let a = localStorage.getItem("note")
        let b =  playC5("K");
        let c = a + ','+b
        //alert('최종 저장된 값: '+ c)
        localStorage.setItem("note", c)
    }

    if(event.keyCode ===79){
        let a = localStorage.getItem("note")
        let b =  playDb5("O");
        let c = a + ','+b
        //alert('최종 저장된 값: '+ c)
        localStorage.setItem("note", c)
    }

    if(event.keyCode ===76){
        let a = localStorage.getItem("note")
        let b =  playD5("L");
        let c = a + ','+b
        //alert('최종 저장된 값: '+ c)
        localStorage.setItem("note", c)
    }

    if(event.keyCode ===80){
        let a = localStorage.getItem("note")
        let b =  playEb5("P");
        let c = a + ','+b
        //alert('최종 저장된 값: '+ c)
        localStorage.setItem("note", c)
    }

    if(event.keyCode ===90){
        let a = localStorage.getItem("note")
        let b =  playE5("Z");
        let c = a + ','+b
        //alert('최종 저장된 값: '+ c)
        localStorage.setItem("note", c)
    }

    if(event.keyCode ===88){
        let a = localStorage.getItem("note")
        let b =  playF5("X");
        let c = a + ','+b
        //alert('최종 저장된 값: '+ c)
        localStorage.setItem("note", c)
    }

    if(event.keyCode ===67){
        let a = localStorage.getItem("note")
        let b =  playGb5("C");
        let c = a + ','+b
        //alert('최종 저장된 값: '+ c)
        localStorage.setItem("note", c)
    }

    if(event.keyCode ===86){
        let a = localStorage.getItem("note")
        let b =  playG5("V");
        let c = a + ','+b
        //alert('최종 저장된 값: '+ c)
        localStorage.setItem("note", c)
    }

    if(event.keyCode ===66){
        let a = localStorage.getItem("note")
        let b =  playAb5("B");
        let c = a + ','+b
        //alert('최종 저장된 값: '+ c)
        localStorage.setItem("note", c)
    }

    if(event.keyCode ===78){
        let a = localStorage.getItem("note")
        let b =  playA5("N");
        let c = a + ','+b
        //alert('최종 저장된 값: '+ c)
        localStorage.setItem("note", c)
    }

    if(event.keyCode ===77){
        let a = localStorage.getItem("note")
        let b =  playBb5("M");
        let c = a + ','+b
        //alert('최종 저장된 값: '+ c)
        localStorage.setItem("note", c)
    }

    if(event.keyCode ===82){
        let a = localStorage.getItem("note")
        let b =  playB5("R");
        let c = a + ','+b
        //alert('최종 저장된 값: '+ c)
        localStorage.setItem("note", c)
    }

    if(event.keyCode ===73){
        let a = localStorage.getItem("note")
        let b =  playC6("I");
        let c = a + ','+b
        //alert('최종 저장된 값: '+ c)
        localStorage.setItem("note", c)
    }
}

export { playC4, playDb4, playD4, playEb4, playE4, playF4, 
playGb4, playG4, playAb4, playA4, playBb4, playB4, playC5,
playDb5, playD5, playEb5, playE5, playF5, playGb5, playG5, 
playAb5, playA5, playBb5, playB5, playC6, PlayNote
}

