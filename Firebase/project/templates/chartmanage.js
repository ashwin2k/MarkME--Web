window.onload = function () {
				chartm();
				updatet();
}
function change()
{
	var inp=document.getElementById("date_inp").value;
	var cf;
	cf=inp.substr(8,2)+'-';
	if(inp.substr(5,2)=="07")
				cf+="Jul";
	else if(inp.substr(5,2)=="08")
				cf+="Aug";
	else
				cf+="Aug";
	cf+='-'+inp.	substr(0,4);
	console.log(cf);
	document.getElementById("sel_date").innerHTML=cf;
	dbget(cf);

}
function dbget(dt)
{
	console.log(firebase.app().name);  // "[DEFAULT]"
	var rollnos=[]
	var db = firebase.firestore();
	var g=document.getElementById("stud_det");
	g.innerHTML="";
	var row=g.insertRow(0);
	var rn=row.insertCell(0);
	rn.outerHTML="<th>Roll No</th>";
	var tm=row.insertCell(1);
	tm.outerHTML="<th>Time</th>";
	pres=0;

		db.collection("Attendance").doc("CSE A").collection(dt).get().then((querySnapshot) => {
			querySnapshot.forEach((doc) => {
				var tab=document.getElementById("stud_det");

				pres++;
				var row=tab.insertRow(1);
				var rn=row.insertCell(0);
				var tm=row.insertCell(1);
				rn.innerHTML=doc.data().ROLL;
				tm.innerHTML=doc.data().UID;
				rollnos.push(doc.data().ROLL);
					console.log(doc.data().ROLL);
			});
			document.getElementById("pres_no").innerHTML=pres;
			console.log("dd"+rollnos);

	});
}
function chartm()
{

	var chart = new CanvasJS.Chart("chartContainer", {
		animationEnabled: true,
		theme: "light2", // "light1", "light2", "dark1", "dark2"
		title:{
			text: "Attendance"
		},
		axisY: {
			title: "Students Present"
		},
		data: [{
			type: "column",
			showInLegend: true,
			legendMarkerColor: "grey",
			legendText: "No of students present around June",
			dataPoints: [
				{ y: 7, label: "8 June" },
				{ y: 0,  label: "10 June" },
				{ y: 0,  label: "11 June" },
				{ y: 8,  label: "12 June" },
				{ y: 12,  label: "13 June" },
				{ y: 11, label: "14 June" },
				{ y: 1,  label: "15 June" },
				{ y: 14,  label: "16 June" }
			]
		}]
	});
	chart.render();

}
function updatet()
{
	setTimeout(updatet,1000);

	var cur= new Date();
	var dat="";
	dat=cur.getHours()+':'+cur.getMinutes();
	if(cur.getHours()<12)
	{
		dat=cur.getHours()+':'+cur.getMinutes()+':'+cur.getSeconds()+"AM";
	}
	else {
			dat=(cur.getHours()-12)+':'+cur.getMinutes()+':'+cur.getSeconds()+"PM";
		}
	document.getElementById("cur_time").innerHTML=dat;
	document.getElementById("cur_date").innerHTML=cur.toDateString();
}
