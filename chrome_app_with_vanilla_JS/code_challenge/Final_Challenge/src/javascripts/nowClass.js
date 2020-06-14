export default class Now{
    constructor(nowContainer){
        this.nowContainer = nowContainer;
        this.date;
    }
    
    today(){
        let y = this.date.getFullYear();
        let m = this.date.getMonth();
        let d = this.date.getDate();
        let day = this.date.getDay();

        if(day == 0) day = "Sun";
        else if(day == 1) day = "Mon";
        else if(day == 2) day = "Tue";
        else if(day == 3) day = "Wed";
        else if(day == 4) day = "Thr";
        else if(day == 5) day = "Fri";
        else if(day == 6) day = "Sat";

        const ret = y + "." + m + "." + d + " " + day;
        return ret;
    }
    clock(){
        let h = this.date.getHours();
        let m = this.date.getMinutes();
        let s = this.date.getSeconds();
        let session = "AM";

        if(h > 12){
            h -= 12;
            session = "PM";
        }
        h = h >= 10 ? h : "0"+ h;
        m = m > 10 ? m : "0"+ m;
        s = s > 10 ? s : "0"+ s;

        const time = session + " " + h + ":" + m + ":" + s;
        return time;
    }
    display(date){
        this.date = new Date();
        this.nowContainer.childNodes[1].innerText = this.today();
        this.nowContainer.childNodes[3].innerText = this.clock();
    }
}
