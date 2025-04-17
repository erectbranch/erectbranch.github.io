function clockPlugin(hook, vm) {
    const days = [
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
    ];
    const months = [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
    ];

    const setTime = () => {
        const time = new Date();
        const date = time.getDate();
        const month = time.getMonth();
        const day = time.getDay();
        const hours = time.getHours();
        const hoursForClock = hours >= 13 ? hours % 12 : hours;
        const hoursForClockWithZero = hoursForClock < 10 ? `0${hoursForClock}` : hoursForClock;

        const minutes = time.getMinutes();
        const seconds = time.getSeconds();
        const ampm = hours >= 12 ? "PM" : "AM";

        const timeElement = document.getElementsByClassName("time")[0];
        const dateElement = document.getElementsByClassName("date")[0];

        const clockConfig = vm.config.clock || {};
        const displaySecond = clockConfig["displaySecond"] || false;
        const displayAMPM = clockConfig["displayAMPM"] || false;

        dateElement.innerHTML = `${days[day]}, ${months[month]} <span class="date-circle">${date}</span>`;
        // {HH}:{MM} or {HH}:{MM}:{SS}
        const minuteSeconds = `${minutes < 10 ? `0${minutes}` : minutes}${displaySecond ? `:${seconds < 10 ? `0${seconds}` : seconds}` : ""}`;

        // {HH(24)}:{MM} or {hh(12)}:{MM} {AM/PM}
        if (displayAMPM) {
            timeElement.innerHTML = `${hoursForClockWithZero}:${minuteSeconds} <span class="am-pm">${ampm}</span>`;
        } else {
            timeElement.innerHTML = `${hours}:${minuteSeconds}`;
        }
    };

    hook.beforeEach((content) => {
        hasClock = content.includes("<!-- clock -->");
        if (!hasClock) return ;

        let clockHtml = `<div class="clock-container">
            <div class="date"></div>
            <div class="time"></div>
        </div>`;

        return content.replace(/<!-- clock -->/gm, clockHtml);
    });

    hook.doneEach(() => {
        setTime();

        setInterval(setTime, 1000);
    });
}

window.$docsify = window.$docsify || {};
window.$docsify.plugins = [].concat(clockPlugin, window.$docsify.plugins)