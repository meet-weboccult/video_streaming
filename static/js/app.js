function start_detection(){
    var socket = io('http://localhost:5000');
    socket.on('connect', function(){
        console.log("Connected...!", socket.connected)
    });
    const video = document.querySelector("#videoElement");
    video.width = 500; 
    video.height = 375; ;

    if (navigator.mediaDevices.getUserMedia) {
        navigator.mediaDevices.getUserMedia({ video: true })
        .then(function (stream) {
            video.srcObject = stream;
            video.play();
        })
        .catch(function (err0r) {
            console.log(err0r)
            console.log("Something went wrong!");
        });
    }

}