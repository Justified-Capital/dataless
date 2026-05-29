## Motivation
The principal at Justified Capital has had almost every part of their life manipulated possible. Especially anything digital that touches the internet-- unfortunately and especially data. Realizing that friendly dataset vendor could actually be the Police, just like the Police have actually been the people at the Secretary of State; masking the truth for their own selfish aims.  A scary reality when they can force places like Google and Stock Brokerages to change data. Polluting the foundational research data like in the image below:


![logo](datalessBowserPolice.png)

So if you assume that an evil actor is taking a giant dump in all your data that touched the internet, how could you possibly create strategies that perform with any degree of reliability in a chaotic environment. An environment that may very well be manipulated against you in the first place.

So if you think about developing strategies from a polluted dataset, no matter what you do- you will lose eventually. In fact, any short-lived success you had was probably just from sheer randomness. A scary truth for any rigorous quant who has tested a strategy against data and then watched it cut to shreds by some market condition that was not reflected at all in data.

The only way to develop rigorous data-driven strategies is to forget datasets along with the Police, and move to a thoughtful preparation of all scenarios that could do meaningful damage to the strategy, along with- of course- those scenarios that provide gains.

### A Math Modeling Analogy
When trying give some degree of predictability, finiteness, and control to a complex non-polynomial function, mathematicians will use a _Taylor Series_ to model a messy function from a context of a base point. Giving some degree of sanity to a local perspective amidst infinite madness. Although a model- there's some order that allows you to draw conclusions that are more sane than trying to pick patterns out of poopy data streams.

Dataless is based on this notion of providing some thoughtful order behind approximating chaos. Creating a series of sequences that represent polynomial outcome paths-- ideally all paths that could meaningfully impact an the outcome of a strategy.

## Getting Started with an Example
Let's say you are researching a strategy called **Gold Digger** that trades off of guaranteed responses in the price of GLD from instability in the rest of the market. You want to ensure that your strategy makes a certain amount of money in good conditions and does not lose more than a certain percentage in bad conditions.

The only way to be sure is to avoid any historical data in favor of using approximations of all possible sequences of prices that could impact your strategy against your goals. That's what `dataless` does; allows you to create sequences in `sequence_modalities.py` and then receive the number of data points that you desire for each specified sequence.

So let's say we want 42 data points for each of the 15 modalities (approximate shapes from percentage changes) sequences for Gold (GLD) with a starting price of 478.34, we would use:
```
dl = DataLess()
data = dl.build_sequences(STARTING_PRICE, DATA_POINT_COUNT)
```

and running `python3 example_usage.py` yields:
```
[487.16, 482.61, 480.27, 479.17, 477.43, 473.88, 475.33, 478.23, 478.04, 481.68, 482.98, 480.27, 478.51, 474.81, 476.03, 471.12, 473.35, 474.52, 477.44, 481.47, 482.17, 480.09, 478.72, 476.2, 472.76, 471.83, 473.99, 475.17, 478.43, 481.73, 481.86, 482.51, 480.23, 478.09, 477.51, 474.37]
[478.48, 481.52, 482.47, 482.74, 481.98, 480.96, 482.47, 483.11, 483.04, 483.99, 485.05, 484.77, 485.12, 482.05, 481.48, 480.17, 483.64, 484.04, 483.78, 484.69, 485.2, 485.93, 485.47, 484.42, 486.57, 485.48, 487.41, 485.83, 487.03, 489.91, 489.95, 490.94, 490.82, 489.37, 491.6, 492.2]
[476.99, 475.15, 477.28, 476.7, 474.73, 475.63, 474.06, 473.55, 471.44, 472.55, 471.49, 471.09, 473.82, 471.72, 475.78, 472.76, 472.15, 471.84, 472.22, 472.63, 471.2, 471.4, 470.1, 471.49, 469.93, 470.83, 468.27, 470.99, 468.94, 466.66, 469.97, 465.97, 467.31, 464.41, 466.97, 465.26]
[481.88, 492.24, 497.75, 506.83, 515.98, 522.7, 516.35, 512.56, 502.97, 496.28, 488.39, 487.8, 487.02, 485.14, 484.4, 483.94, 486.29, 484.99, 483.28, 481.21, 483.08, 481.77, 478.39, 478.02, 475.28, 474.08, 475.74, 477.0, 478.96, 481.85, 482.32, 482.88, 483.2, 486.53, 487.9, 485.94]
[480.77, 484.5, 482.93, 483.27, 485.24, 487.43, 489.8, 494.53, 499.78, 502.54, 509.89, 505.26, 498.61, 494.99, 491.35, 483.68, 485.18, 484.11, 483.04, 485.1, 482.56, 481.64, 481.25, 484.75, 483.96, 482.89, 480.99, 480.47, 480.51, 476.18, 476.77, 478.09, 479.95, 481.53, 480.35, 482.6]
[480.74, 481.68, 482.21, 481.01, 482.45, 483.16, 484.2, 481.24, 481.38, 480.7, 476.92, 480.01, 481.8, 483.32, 485.17, 483.71, 483.99, 484.63, 486.64, 488.43, 487.56, 488.82, 487.96, 486.26, 488.33, 485.44, 491.01, 496.44, 502.7, 505.48, 514.23, 509.69, 504.02, 498.84, 497.12, 490.9]
[482.11, 484.5, 486.27, 488.86, 492.42, 495.73, 493.06, 490.98, 492.5, 488.95, 488.39, 488.3, 488.34, 486.95, 487.38, 486.35, 482.85, 483.0, 484.4, 481.32, 482.42, 478.84, 477.71, 477.33, 476.5, 471.13, 473.01, 475.68, 480.8, 482.06, 482.66, 483.37, 484.48, 484.82, 485.03, 486.11]
[482.97, 482.87, 483.61, 483.76, 484.94, 485.82, 486.91, 492.39, 492.57, 495.83, 496.37, 492.63, 492.94, 491.11, 487.66, 486.45, 484.63, 484.46, 484.8, 481.14, 480.86, 481.47, 481.96, 481.49, 481.77, 484.53, 482.6, 481.66, 477.94, 479.72, 476.75, 478.95, 478.65, 478.86, 480.65, 484.02]
[481.82, 481.61, 482.61, 484.34, 482.49, 482.12, 483.24, 479.89, 481.35, 479.53, 476.01, 478.33, 478.72, 482.85, 483.19, 484.34, 485.49, 484.49, 482.99, 484.44, 485.58, 485.89, 486.34, 486.11, 486.31, 486.12, 486.54, 491.87, 493.7, 493.15, 497.68, 496.69, 491.85, 493.78, 492.12, 490.43]
[473.54, 467.05, 461.32, 456.23, 448.53, 443.93, 447.2, 453.65, 456.24, 463.94, 465.89, 466.44, 467.09, 470.78, 471.94, 472.97, 472.46, 472.97, 471.99, 473.43, 473.4, 472.01, 472.23, 474.25, 474.23, 473.3, 470.56, 471.96, 471.6, 469.25, 469.37, 468.92, 470.85, 470.84, 471.39, 470.3]
[484.13, 478.93, 477.0, 476.24, 473.11, 471.38, 466.97, 459.54, 457.97, 453.02, 446.59, 451.41, 457.81, 463.62, 467.55, 472.16, 473.36, 476.19, 475.03, 479.04, 480.14, 479.35, 477.34, 476.89, 474.5, 472.75, 472.04, 474.13, 475.67, 473.97, 475.03, 477.69, 474.56, 473.81, 474.74, 473.7]
[475.09, 476.55, 477.13, 478.63, 482.14, 482.54, 482.03, 478.35, 479.64, 477.11, 478.86, 478.99, 480.15, 479.71, 480.93, 485.11, 480.79, 478.87, 477.63, 477.85, 473.39, 473.31, 470.92, 472.93, 469.83, 470.37, 466.46, 462.65, 457.24, 452.97, 449.15, 452.69, 456.83, 461.14, 467.65, 471.06]
[475.36, 473.67, 467.59, 465.97, 460.64, 456.92, 458.47, 462.55, 464.91, 464.95, 467.28, 466.42, 471.1, 472.19, 472.98, 473.88, 475.02, 475.05, 472.85, 473.01, 474.43, 473.55, 474.74, 473.77, 474.7, 473.78, 474.53, 474.08, 474.95, 474.86, 478.21, 476.26, 474.51, 474.37, 473.84, 470.35]
[483.59, 480.9, 475.78, 475.35, 473.24, 468.85, 470.08, 466.19, 463.6, 463.74, 461.2, 463.3, 463.89, 465.05, 470.83, 470.4, 470.8, 471.65, 471.88, 472.55, 474.39, 471.97, 474.15, 473.34, 474.77, 471.23, 475.21, 474.29, 479.1, 476.91, 479.61, 479.53, 478.17, 477.96, 474.09, 473.42]
[481.79, 480.48, 479.5, 477.71, 477.74, 474.39, 474.97, 478.45, 475.86, 479.4, 480.58, 479.15, 475.87, 477.23, 473.39, 473.38, 473.12, 477.67, 475.61, 478.67, 481.34, 478.57, 476.45, 475.61, 471.82, 471.53, 468.78, 467.77, 462.78, 461.95, 458.49, 460.28, 464.98, 464.95, 469.84, 470.65]
```

which represents data for each modality mapped to `sequence_modalities.py` illustrated below:

<img width="784" height="1083" alt="image" src="https://github.com/user-attachments/assets/86117db8-a665-4058-a316-b41a6aa7e01f" />

Noting that you can change that sequences modalities- adding, editing, and deleting as you please- as long as you keep the same structure.
