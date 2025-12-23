# 🏞️  Momentum changes due to "added mass" and "wake momentum"
As noted, the term on the *right hand side* of Newton's 2nd Law is $ \mathit{mass} \times \mathit{acceleration}$, representing the rate of change of [**momentum**](wiki:momentum)[^1].
Momentum is the product of mass times acceleration.


One contribution to momentum comes from the mass of the organism or particle.
In familiar terms, the mass of a bowling ball is much greater than the mass of a ping-pong ball, so the bowling ball has much more momentum than the ping-pong ball if they are traveling at the same velocity.

In most applications in Organismal Biology, an organism's mass is more or less constant over short periods.
In that case, changes in the organism's momentum result from changes in its velocity[^2].

However, for organisms immersed in fluids, there is another factor: *To move, an organism or any other particle must also displace fluid around itself.*
The water that is moved in concert with an organism must be accounted for in assessing the relationship between forces and movement.
There are two primary ways in which moving fluid affects the righthand side terms of Newton's 2nd Law: *Added mass*, and *wake momentum*.
Understanding these concepts will be very helpful when thinking about the biomechanics of organism movement in fluids.

## Added mass
If you have seen a person rowing a boat (or had a chance to row one yourself) you have seen the shape of an oar.
At one end the oar has a handle, where it is gripped by the rower. 
At the other end, the oar is the "blade", which is wide and flat but quite thin. 

To propel the boat, the rower inserts the oar into the water with the blade perpendicular to the direction the boat is moving, before pulling. 
It is intuitive that this is necessary to row effectively &ndash; if the blade were parallel to the direction of motion, it would slice easily through the water and provide very little propulsion.

Despite it being intuitive, few people (including rowers) have thought about *why this is the case*?
When an oar is pulled through the water, its mass is the same whether it's perpendicular or parallel to the direction of motion. 
What then is the difference?

The difference is [added mass](wiki:Added_mass), the engineering term for fluid that must be moved when an object moves through a fluid.
For example, when the oar is pulled in a perpendicular position, water next to the front and back of the blade moves with it. 
Because the perpendicular blade has a large area in line with its motion, this is a lot of water.
This water is the added mass of the oar.
Accelerating this added mass of water is what makes the oar effective, and oars are designed specifically to have large added mass when pulled in the perpendicular position.

In contrast, the parallel blade has a small area in line with its motion, so it moves relatively little water.
That is, it has little added mass. 
It is said to be *streamlined*, which means it moves with little resistance through the fluid.

In a well-designed oar, the added mass in its "power" orientation is much larger than the mass of the blade itself.
The same is true of many appendages of organisms that propell themselves through water. 
While other fluid dynamical mechanisms are also operating, thinking in terms of added mass often provides useful insights into the biomechanics of movement through fluids.

## Wake momentum
Standing in an exposed spot on a very windy day, you can feel the pressure of the wind pushing you downwind.
Since you are stationary and not accelerating, your momentum is constant and its rate of change is zero.
Newton's 2nd Law says that if your momentum is not changing, the sum of forces on you must be zero.
However there is quite definitely a wind force acting on you.
How does this make sense?

It makes sense because, though your body's momentum is not changing, by blocking the wind you are constantly changing the momentum of the air around you.
Specifically, you are creating a [wake](wiki:Wake_(physics)) downwind of yourself, and that wake has less momentum than the air that is approaching you from upwind.

To understand the basic mechanism, let's think about a simplified geometry:
Let's assume that your have a profile area (perpendicular to the wind) of $1m^2$.
The wind speed upwind of you is $10 \frac{m}{s}$ (about $11 mph$).
That means roughly $10 m^3$ of air, corresponding to a little over $12 kg$, is encountering your body every second.
The momentum in that air is $10 m^3 \times 12 kg$ &ndash; a considerable amount.

However your body is blocking that air, so that downstream of you there is a zone in which wind speed is greatly reduced.
If the air in this zone has zero velocity (an oversimplification, but still a useful rough estimate) then, by blocking the wind, you are subtracting $120 m^3kg$ of momentum each second from the air as it passes you.
This requires force, that is the force that you feel as wind pressure and provide by opposing it with your feet.

This idea &ndash; that a moving organism creates a wake that requires force to maintain even if its own momentum is constant &ndash; is key to understanding both how organisms are shaped by evolution to minimize costs of locomotion and how forces on moving organisms scale with basic characteristics such as size and velocity.

## Summary
To sum up, an object moving in a fluid has additional "apparent" contributions to its momentum, as accounted for in Newton's 2nd Law.
This is because:
1. When it accelerates, it also accelerates some of the fluid around it; the mass of this fluid is called "added mass".
2. As it moves through the fluid, it leaves behind it a wake of fluid it has accelerated to its own velocity; to continually change the momentum of the fluid it encounters (the "wake momentum") requires force, which the object experiences as drag.

Added mass and wake momentum are continually acting on our own bodies, because we are immersed in a fluid (air). 
Because our bodies are so much denser than air, we usually don't feel these effects, but under some circumstances (bicycling, swimming, windy days, *etc.*) they become much more noticeable.


[^1]: Some references refer to [inertia](wiki:inertia) as a synonym for momentum. Inertia is defined slightly differently, but is a closely related concept. Some references refer to momentum effects as an [inertial force](wiki:Fictitious_force). These effects are is not really a force, but it has units of force, and some references find it convenient to use this shorthand (while keeping in mind its actual interpretation). 
[^2]:In some cases, though, changes in mass during acceleration are important. Examples include the swimming biomechanics of "jet-propelled" animals like squid and jellyfish, in which water that initially is enclosed and moves with the organism is left behind during a muscular contraction to produce thrust.
 
