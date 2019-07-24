$(document).ready(function(){

		$("#try-again").click(resetQuiz);
		$("#submit-form").click(processResults);
		let description= null;
		let portrait = null;
		

	function getPersonality(){

		let score = 0
		let personality = null;
	   		
		let bullyDictionary = {
			q1a: 4,
			q1b: 3,
			q1c: 2,
			q1d: 1
		};
		let bossDictionary = {
			q2a: 4,
			q2b: 3,
			q2c: 2,
			q2d: 1
		};
		let weaponDictionary = {
			q3a: 4,
			q3b: 3,
			q3c: 2,
			q3d: 1
		};
		let lifestyleDictionary = {
			q4a: 4,
			q4b: 3,
			q4c: 2,
			q4d: 1
		};
		let animeDictionary = {
			q5a: 4,
			q5b: 3,
			q5c: 2,
			q5d: 1
		};

		let q1 = $('input[name="q1"]:checked').attr('id');    
		let q2 = $('input[name="q2"]:checked').attr('id'); 
		let q3 = $('input[name="q3"]:checked').attr('id');
		let q4 = $('input[name="q4"]:checked').attr('id');
		let q5 = $('input[name="q5"]:checked').attr('id');

		score += bullyDictionary[q1]+ bossDictionary[q2]+ weaponDictionary[q3]+ lifestyleDictionary[q4]+ animeDictionary[q5];

		console.log(q1);
		console.log(q2);
		console.log(q3);
		console.log(q4);
		console.log(q5);
		console.log(score);

		if(score<=20 && score>=16){
			personality="Tsuna";
			description = "You are someone who's life doesn't always go right, but you know you'll be fine with your friends in the end. You only fight for your friends";
			portrait = "tsuna-san.jpg";
			console.log(personality);
		}
		else if(score<=16 && score>=11){
			personality="Gokudera";
			description = "You are someone who can only be open with few people. Otherwise you push people away and act like a delinquent, when truly you care. You fight to be there for your friends";
			portrait = "gokudera-san.jpg";
			console.log(personality);
		}
		else if(score<=10 && score>=6){
			personality="Yamamoto";
			description = "You are a happy go lucky person who is always positive. You show ignorance as your bravery for your friends even if you know you guys are in trouble. You fight to be a hero";
			portrait = "yamamoto-san.jpg";
			console.log(personality);
		}
		else if(score<=5 && score>=0){
			personality="Hibari";
			description="You are a distant warrior. You are mysterious. All fear you, and you distance yourself from crowds. You have pure heart...pure unadulturated wrath. You fight to fight.";
			portrait = "hibari-san.jpg";
			console.log(personality);
		}
		return personality;

	}
		
	function processResults(){
				let q1 = $('input[name="q1"]:checked').attr('id');    
				let q2 = $('input[name="q2"]:checked').attr('id'); 
				let q3 = $('input[name="q3"]:checked').attr('id');
				let q4 = $('input[name="q4"]:checked').attr('id');
				let q5 = $('input[name="q5"]:checked').attr('id');
				if(q1==null||q2==null||q3==null||q4==null||q5==null){
					alert("Shtop being shtupid! Answer all the ?'s!");
				}
				else{
				let personality = getPersonality();
				$("#quiz-wrapper").hide();
				$("#results").show();
				$("#try-again").show();
				$("#results").append("<h1>Congrats! Your personality is " +personality+"!</h1>");
				$("#results").append("<h1> "+description+":)</h1>");				
				$("#results").append('<img src="'+portrait+'">');
				}
	}


	function resetQuiz(){
		$("#try-again").hide();
		$("#results").hide();
		$("#quiz-wrapper").show();
		q1:checked=false;
		q2:checked=false;
		q3:checked=false;
		q4:checked=false;
		q5:checked=false;
	}




});
