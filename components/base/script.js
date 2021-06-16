'use strict';

// Global components list
let components = window.components = {};

components.fonts = {
	selector: 'html',
	styles: 'https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap'
};

components.mdi = {
	selector: '[class*="mdi"]',
	styles: './components/mdi/mdi.css'
};

components.grid = {
	selector: '.container, .container-fluid, .row, [class*="col-"]',
	styles: './components/grid/grid.css'
};

components.block = {
	selector: '.block',
	styles: './components/block/block.css'
};

components.blurb = {
	selector: '.blurb',
	styles: [
		'./components/media/media.css',
		'./components/blurb/blurb.css'
	]
};

components.box = {
	selector: '.box',
	styles: './components/box/box.css'
};

components.button = {
	selector: '.btn, .btn-group',
	styles: './components/button/button.css'
};

components.divider = {
	selector: '.divider',
	styles: './components/divider/divider.css'
};

components.form = {
	selector: '.form-group, .input-group, .form-check, .custom-control, .form-control',
	styles: './components/form/form.css'
};

components.formOutput = {
	selector: '.form-output',
	styles:   './components/form-output/form-output.css'
};

components.icon = {
	selector: '.icon',
	styles: './components/icon/icon.css'
};

components.imageSvg = {
	selector: '.image-svg',
	styles: './components/image-svg/image-svg.css'
};

components.list = {
	selector: '.list',
	styles: './components/list/list.css'
};

components.media = {
	selector: '.media',
	styles: './components/media/media.css'
};

components.partner = {
	selector: '.partner',
	styles: './components/partner/partner.css'
};

components.post = {
	selector: '.post, .post-modern',
	styles: './components/post/post.css'
};

components.pricing = {
	selector: '.pricing, .pricing-modern',
	styles: './components/pricing/pricing.css'
};

components.quote = {
	selector: '.quote',
	styles: [
		'./components/media/media.css',
		'./components/quote/quote.css'
	]
};

components.rights = {
	selector: '.rights',
	styles: './components/rights/rights.css'
};

components.section = {
	selector: 'section',
	styles: './components/section/section.css'
};

components.snackbar = {
	selector: '.snackbar',
	styles: './components/snackbar/snackbar.css'
};

components.table = {
	selector: '.table',
	styles: './components/table/table.css'
};

components.team = {
	selector: '.team, .team-mini',
	styles: './components/team/team.css'
};

components.video = {
	selector: '.video',
	styles: './components/video/video.css'
};

components.accordion = {
	selector: '.accordion',
	styles: './components/accordion/accordion.css',
	script: [
		'./components/jquery/jquery.min.js',
		'./components/current-device/current-device.min.js',
		'./components/multiswitch/multiswitch.min.js'
	],
	init: function ( nodes ) {
		nodes.forEach( function ( node ) {
			let
				items = node.querySelectorAll( '.accordion-item' ),
				click = device.ios() ? 'touchstart' : 'click';

			items.forEach( function ( item ) {
				let
					head = item.querySelector( '.accordion-head' ),
					body = item.querySelector( '.accordion-body' );

				MultiSwitch({
					node: head,
					targets: [ item, body ],
					isolate: node.querySelectorAll( '.accordion-head' ),
					state: item.classList.contains( 'active' ),
					event: click,
				});

				if ( !body.multiSwitchTarget.groups.active.state ) body.style.display = 'none';

				body.addEventListener( 'switch:active', function () {
					let $this = $( this );

					if ( this.multiSwitchTarget.groups.active.state ) {
						$this.stop().slideDown( 300 );
					} else {
						$this.stop().slideUp( 300 );
					}
				});
			});
		});
	}
};

components.animate = {
	selector: '[data-animate]',
	styles: './components/animate/animate.css',
	script: './components/current-device/current-device.min.js',
	init: function ( nodes ) {
		let observer = new IntersectionObserver( function ( entries, observer ) {
			entries.forEach( function ( entry ) {
				let node = entry.target;

				if ( entry.isIntersecting ) {
					node.animationStart();
					observer.unobserve( node );
				}
			});
		});

		nodes.forEach( function ( node ) {
			let params = parseJSON( node.getAttribute( 'data-animate' ) );
			params.class = params.class ? [ 'animated' ].concat( params.class ) : [ 'animated' ];
			if ( params.delay ) { node.style.animationDelay = params.delay; }
			if ( params.duration ) { node.style.animationDuration = params.duration; }

			node.animationStart = ( function () {
				this.classList.add.apply( this.classList, params.class );
			}).bind( node );

			observer.observe( node );
		});
	}
};

components.countdown = {
	selector: '[data-countdown]',
	styles: './components/countdown/countdown.css',
	script: [
		'./components/progress-circle/progress-circle.min.js',
		'./components/countdown/countdown.min.js'
	],
	init: function ( nodes ) {
		nodes.forEach( function ( node ) {
			new Countdown( strictMerge({
				node: node,
				from: null,
				to: null,
				count: 'auto',
				tick: 100
			}, parseJSON( node.getAttribute( 'data-countdown' ) ) ) );
		} )
	}
};

components.counter = {
	selector: '[data-counter]',
	styles: './components/counter/counter.css',
	script: './components/counter/counter.min.js',
	init: function ( nodes ) {
		let observer = new IntersectionObserver( function ( entries, observer ) {
			entries.forEach( function ( entry ) {
				let node = entry.target;

				if ( entry.isIntersecting ) {
					node.counter.run();
					observer.unobserve( node );
				}
			});
		}, {
			rootMargin: '0px',
			threshold: 1.0
		});

		nodes.forEach( function ( node ) {
			let counter = new bCounter( Object.assign( {
				node: node,
				duration: 1000,
				autorun: false
			}, parseJSON( node.getAttribute( 'data-counter' ) ) ) );

			if ( window.xMode ) {
				counter.run();
			} else {
				observer.observe( node );
			}
		})
	}
};

// components.blotter = {
// 	selector: '#blotter',
// 	script: [
// 		'./components/jquery/jquery.min.js',
// 		'./components/blotter/blotter.min.js',
// 		'./components/blotter/liquidDistortMaterial.js'
// 	],
// 	init: function () {
// 		let text = new Blotter.Text( 'observation', {
// 			family : "'EB Garamond', serif",
// 			size : 120,
// 			fill : "#fff"
// 		});
//
// 		var material = new Blotter.LiquidDistortMaterial();
//
// 		material.uniforms.uSpeed.value = 0;
//
// 		let blotter = new Blotter( material, {
// 			texts : text
// 		});
//
// 		let
// 			elem = document.getElementById( 'blotter' ),
// 			scope = blotter.forText( text );
//
// 		scope.appendTo( elem );
//
// 		elem.addEventListener( 'mouseover', function() {
// 			material.uniforms.uSpeed.value = 0.25;
// 		} );
//
// 		elem.addEventListener( 'mouseleave', function() {
// 			material.uniforms.uSpeed.value = 1;
// 		} );
// 	}
// };

// TODO move to blurb component
components.currentDevice = {
	selector: 'html',
	script: './components/current-device/current-device.min.js'
};

components.fullpage = {
	selector: '.fullpage',
	styles: './components/fullpage/fullpage.css',
	script: [
		'./components/jquery/jquery.min.js',
		'./components/fullpage/fullpage.min.js',
		'./components/util/util.min.js'
	],
	init: function ( nodes ) {
		nodes.forEach( function ( node ) {
			let
				timerId = null,
				animationIsFinished = false,
				state = null,
				newState = null,
				defaults = {
					navigation: true,
					navigationPosition: 'left',
					easingcss3: 'ease-in',
					// afterLoad: function ( anchorLink, index ) {
					// 	let
					// 		section = node.children[ index - 1 ],
					// 		animations = section.querySelectorAll( '[data-animate], .layer' );
					//
					// 	if ( animations.length ) {
					// 		animations.forEach( function ( node ) {
					// 			node.animate();
					// 		});
					// 	}
					//
					// 	animationIsFinished = false;
					// },
					// onLeave: function( index, nextIndex ) {
					// 	if ( !animationIsFinished && !timerId ) {
					// 		let
					// 			section = node.children[ index - 1 ],
					// 			animations = section.querySelectorAll( '[data-animate], .layer' );
					//
					// 		if ( animations.length ) {
					// 			animations.forEach( function ( node ) {
					// 				node.reanimate();
					// 			});
					// 		}
					//
					// 		timerId = setTimeout( function() {
					// 			animationIsFinished = true;
					// 			$.fn.fullpage.moveTo( nextIndex );
					// 			timerId = null;
					// 		}, 600 );
					// 	}
					//
					// 	return animationIsFinished;
					// }
				},
				mobile = {
					navigation: false,
					paddingTop: '60px'
				},
				resizeHandler = function () {
					if ( window.matchMedia("( min-width: 1200px )").matches ) {
						newState = 'desktop';
					} else {
						newState = 'mobile';
					}

					if ( state !== newState ) {
						if ( document.documentElement.classList.contains( 'fp-enabled' ) ) $.fn.fullpage.destroy( 'all' );
						state = newState;

						switch( state ) {
							case 'desktop':
								$( node ).fullpage( defaults );
								break;
							case 'mobile':
								$( node ).fullpage( Object.assign( defaults, mobile ) );
								break;
						}
					}
				};

			resizeHandler();
			window.addEventListener( 'resize', resizeHandler );
		});
	}
};

components.imageHover = {
	selector: '.image-hover',
	styles: './components/image-hover/image-hover.css',
	script: [
		'https://cdnjs.cloudflare.com/ajax/libs/gsap/1.20.3/TweenMax.min.js',
		'./components/image-hover/three.min.js',
		'./components/image-hover/hover.js'
	],
	init: function ( nodes ) {
		nodes.forEach( function ( node ) {
			let
				img = node.querySelector( 'img' ),
				imgSrcFrom = img.getAttribute( 'src' ),
				imgSrcTo = img.getAttribute( 'data-image-to' );

			new hoverEffect({
				parent: node,
				intensity: -0.2,
				speedIn: 1.2,
				image1: imgSrcFrom,
				image2: imgSrcTo ? imgSrcTo : imgSrcFrom,
				displacementImage: 'components/image-hover/displacement/4.png'
			});
		});
	}
};

components.lightgallery = {
	selector: '[data-lightgallery]',
	styles: './components/lightgallery/lightgallery.css',
	script: [
		'./components/jquery/jquery.min.js',
		'./components/lightgallery/lightgallery.min.js'
	],
	init: function ( nodes ) {
		if ( !window.xMode ) {
			nodes.forEach( function ( node ) {
				let
					$node = $( node ),
					params = merge( {
						selector: 'this',
						hash: false
					}, parseJSON( $node.attr( 'data-lightgallery' ) ) );

				if ( params.dynamic ) {
					node.addEventListener( 'click', function () {
						$node.lightGallery( params );
					});
				} else {
					$node.lightGallery( params );
				}
			});
		}
	}
};

components.modalBtn = {
	selector: '[data-modal-trigger]',
	dependencies: 'modal',
	init: function ( nodes ) {
		nodes.forEach( function ( node ) {
			let params = parseJSON( node.getAttribute( 'data-modal-trigger' ) );

			node.addEventListener( 'click', function () {
				let modal = document.querySelector( params.target );
				if ( modal.classList.contains( 'show' ) ) {
					$( modal ).modal( 'hide' );
				} else {
					$( modal ).modal( 'show' );
				}
			});
		});
	}
};

components.modal = {
	selector: '.modal',
	styles: './components/modal/modal.css',
	script: [
		'./components/jquery/jquery.min.js',
		'./components/bootstrap/js/popper.min.js',
		'./components/bootstrap/js/bootstrap.min.js'
	],
	init: function ( nodes ) {
		nodes.forEach( function ( node ) {
			$( node ).modal({
				show: false,
				focus: false
			});
		});
	}
};

components.multiswitch = {
	selector: '[data-multi-switch]',
	styles: './components/multiswitch/multiswitch.css',
	script: [
		'./components/current-device/current-device.min.js',
		'./components/multiswitch/multiswitch.min.js'
	],
	dependencies: 'rdNavbar',
	init: function ( nodes ) {
		let click = device.ios() ? 'touchstart' : 'click';

		nodes.forEach( function ( node ) {
			if ( node.tagName === 'A' ) {
				node.addEventListener( click, function ( event ) {
					event.preventDefault();
				});
			}

			MultiSwitch( Object.assign( {
				node: node,
				event: click,
			}, parseJSON( node.getAttribute( 'data-multi-switch' ) ) ) );
		});
	}
};

components.nav = {
	selector: '.nav',
	styles: './components/nav/nav.css',
	script: [
		'./components/jquery/jquery.min.js',
		'./components/bootstrap/js/popper.min.js',
		'./components/bootstrap/js/bootstrap.min.js'
	],
	init: function ( nodes ) {
		nodes.forEach( function ( node ) {
			$( node ).on( 'click', function ( event ) {
				event.preventDefault();
				$( this ).tab( 'show' );
			});

			$( node ).find( 'a[data-toggle="tab"]' ).on( 'shown.bs.tab', function () {
				window.dispatchEvent( new Event( 'resize' ) );
			});
		});
	}
};

components.owl = {
	selector: '.owl-carousel',
	styles: './components/owl-carousel/owl.carousel.css',
	script: [
		'./components/jquery/jquery.min.js',
		'./components/owl-carousel/owl.carousel.min.js',
		'./components/util/util.min.js'
	],
	init: function ( nodes ) {
		nodes.forEach( function ( node ) {
			let
				params = parseJSON( node.getAttribute( 'data-owl' ) ),
				defaults = {
					items: 1,
					margin: 30,
					loop: true,
					mouseDrag: true,
					stagePadding: 0,
					nav: false,
					navText: [],
					dots: false,
					autoplay: true,
					autoplayHoverPause: true
				},
				xMode = {
					autoplay: false,
					loop: false,
					mouseDrag: false
				};

			node.owl = $( node );

			let tmp = Util.merge( window.xMode ? [ defaults, params, xMode ] : [ defaults, params ] );

			$( node ).owlCarousel( tmp );
		});
	}
};

components.pageReveal = {
	selector: 'html',
	init: function( nodes ) {
		window.addEventListener( 'components:ready', function () {
			window.dispatchEvent( new CustomEvent( 'resize' ) );
			document.documentElement.classList.add( 'components-ready' );

			setTimeout( function() {
				document.documentElement.classList.add( 'page-loaded' );
			}, 300 );
		}, { once: true } );
	}
};

components.rdMailform = {
	selector: '.rd-mailform',
	styles: [
		'./components/rd-mailform/rd-mailform.css',
		'./components/font-awesome/font-awesome.css',
		'./components/mdi/mdi.css'
	],
	script: [
		'./components/jquery/jquery.min.js',
		'./components/rd-mailform/rd-mailform.min.js',
	],
	init: function ( nodes ) {
		let i, j, k,
			$captchas = $( nodes ).find( '.recaptcha' ),
			msg = {
				'MF000': 'Successfully sent!',
				'MF001': 'Recipients are not set!',
				'MF002': 'Form will not work locally!',
				'MF003': 'Please, define email field in your form!',
				'MF004': 'Please, define type of your form!',
				'MF254': 'Something went wrong with PHPMailer!',
				'MF255': 'Aw, snap! Something went wrong.'
			};

		if ( $captchas.length ) {
			$.getScript("//www.google.com/recaptcha/api.js?onload=onloadCaptchaCallback&render=explicit&hl=en");
		}

		/**
		 * @desc Check if all elements pass validation
		 * @param {object} elements - object of items for validation
		 * @param {object} captcha - captcha object for validation
		 * @return {boolean}
		 */
		function isValidated(elements, captcha) {
			let results, errors = 0;

			if (elements.length) {
				for (let j = 0; j < elements.length; j++) {

					let $input = $(elements[j]);
					if ((results = $input.regula('validate')).length) {
						for (k = 0; k < results.length; k++) {
							errors++;
							$input.siblings(".form-validation").text(results[k].message).parent().addClass("has-error");
						}
					} else {
						$input.siblings(".form-validation").text("").parent().removeClass("has-error");
					}
				}

				if (captcha) {
					if (captcha.length) {
						return validateReCaptcha(captcha) && errors === 0
					}
				}

				return errors === 0;
			}
			return true;
		}

		/**
		 * @desc Validate google reCaptcha
		 * @param {object} captcha - captcha object for validation
		 * @return {boolean}
		 */
		function validateReCaptcha(captcha) {
			let captchaToken = captcha.find('.g-recaptcha-response').val();

			if (captchaToken.length === 0) {
				captcha
					.siblings('.form-validation')
					.html('Please, prove that you are not robot.')
					.addClass('active');
				captcha
					.closest('.form-wrap')
					.addClass('has-error');

				captcha.on('propertychange', function () {
					let $this = $(this),
						captchaToken = $this.find('.g-recaptcha-response').val();

					if (captchaToken.length > 0) {
						$this
							.closest('.form-wrap')
							.removeClass('has-error');
						$this
							.siblings('.form-validation')
							.removeClass('active')
							.html('');
						$this.off('propertychange');
					}
				});

				return false;
			}

			return true;
		}

		/**
		 * @desc Initialize Google reCaptcha
		 */
		window.onloadCaptchaCallback = function () {
			for (let i = 0; i < $captchas.length; i++) {
				let
					$captcha = $($captchas[i]),
					resizeHandler = (function() {
						let
							frame = this.querySelector( 'iframe' ),
							inner = this.firstElementChild,
							inner2 = inner.firstElementChild,
							containerRect = null,
							frameRect = null,
							scale = null;

						inner2.style.transform = '';
						inner.style.height = 'auto';
						inner.style.width = 'auto';

						containerRect = this.getBoundingClientRect();
						frameRect = frame.getBoundingClientRect();
						scale = containerRect.width/frameRect.width;

						if ( scale < 1 ) {
							inner2.style.transform = 'scale('+ scale +')';
							inner.style.height = ( frameRect.height * scale ) + 'px';
							inner.style.width = ( frameRect.width * scale ) + 'px';
						}
					}).bind( $captchas[i] );

				grecaptcha.render(
					$captcha.attr('id'),
					{
						sitekey: $captcha.attr('data-sitekey'),
						size: $captcha.attr('data-size') ? $captcha.attr('data-size') : 'normal',
						theme: $captcha.attr('data-theme') ? $captcha.attr('data-theme') : 'light',
						callback: function () {
							$('.recaptcha').trigger('propertychange');
						}
					}
				);

				$captcha.after("<span class='form-validation'></span>");

				if ( $captchas[i].hasAttribute( 'data-auto-size' ) ) {
					resizeHandler();
					window.addEventListener( 'resize', resizeHandler );
				}
			}
		};

		for ( i = 0; i < nodes.length; i++ ) {
			let
				$form = $(nodes[i]),
				formHasCaptcha = false;

			$form.attr('novalidate', 'novalidate').ajaxForm({
				data: {
					"form-type": $form.attr("data-form-type") || "contact",
					"counter": i
				},
				beforeSubmit: function (arr, $form, options) {
					let
						form = $(nodes[this.extraData.counter]),
						inputs = form.find("[data-constraints]"),
						output = $("#" + form.attr("data-form-output")),
						captcha = form.find('.recaptcha'),
						captchaFlag = true;

					output.removeClass("active error success");

					if (isValidated(inputs, captcha)) {

						// veify reCaptcha
						if (captcha.length) {
							let captchaToken = captcha.find('.g-recaptcha-response').val(),
								captchaMsg = {
									'CPT001': 'Please, setup you "site key" and "secret key" of reCaptcha',
									'CPT002': 'Something wrong with google reCaptcha'
								};

							formHasCaptcha = true;

							$.ajax({
								method: "POST",
								url: "components/rd-mailform/reCaptcha.php",
								data: {'g-recaptcha-response': captchaToken},
								async: false
							})
								.done(function (responceCode) {
									if (responceCode !== 'CPT000') {
										if (output.hasClass("snackbar")) {
											output.html('<div class="snackbar-inner"><div class="snackbar-title"><span class="icon snackbar-icon mdi-check"></span>'+ captchaMsg[responceCode] +'</div></div>');

											setTimeout(function () {
												output.removeClass("active");
											}, 3500);

											captchaFlag = false;
										} else {
											output.html(captchaMsg[responceCode]);
										}

										output.addClass("active");
									}
								});
						}

						if (!captchaFlag) {
							return false;
						}

						form.addClass('form-in-process');

						if (output.hasClass("snackbar")) {
							// output.html('<p><span class="icon text-middle fa fa-circle-o-notch fa-spin icon-xxs"></span><span>Sending</span></p>');
							output.html('<div class="snackbar-inner"><div class="snackbar-title"><span class="icon snackbar-icon fa-circle-o-notch fa-spin"></span>Sending</div></div>');
							output.addClass("active");
						}
					} else {
						return false;
					}
				},
				error: function (result) {
					let output = $("#" + $(nodes[this.extraData.counter]).attr("data-form-output")),
						form = $(nodes[this.extraData.counter]);

					output.text(msg[result]);
					form.removeClass('form-in-process');

					if (formHasCaptcha) {
						grecaptcha.reset();
					}
				},
				success: function (result) {
					let form = $(nodes[this.extraData.counter]),
						output = $("#" + form.attr("data-form-output")),
						select = form.find('select');

					form
						.addClass('success')
						.removeClass('form-in-process');

					if (formHasCaptcha) {
						grecaptcha.reset();
					}

					result = result.length === 5 ? result : 'MF255';
					output.text(msg[result]);

					if (result === "MF000") {
						if (output.hasClass("snackbar")) {
							output.html('<div class="snackbar-inner"><div class="snackbar-title"><span class="icon snackbar-icon mdi-check"></span>'+ msg[result] +'</div></div>');
						} else {
							output.addClass("active success");
						}
					} else {
						if (output.hasClass("snackbar")) {
							output.html('<div class="snackbar-inner"><div class="snackbar-title"><span class="icon snackbar-icon mdi-alert-outline"></span>'+ msg[result] +'</div></div>');
						} else {
							output.addClass("active error");
						}
					}

					form.clearForm();

					if (select.length) {
						select.select2("val", "");
					}

					form.find('input, textarea').trigger('blur');

					setTimeout(function () {
						output.removeClass("active error success");
						form.removeClass('success');
					}, 3500);
				}
			});
		}
	}
};

components.rdNavbar = {
	selector: '.rd-navbar',
	styles: './components/rd-navbar/rd-navbar.css',
	script: [
		'./components/jquery/jquery.min.js',
		'./components/util/util.min.js',
		'./components/current-device/current-device.min.js',
		'./components/rd-navbar/rd-navbar.min.js'
	],
	dependencies: 'currentDevice',
	init: function ( nodes ) {
		nodes.forEach( function ( node ) {
			let
				backButtons = node.querySelectorAll( '.navbar-navigation-back-btn' ),
				params = parseJSON( node.getAttribute( 'data-rd-navbar' ) ),
				defaults = {
					stickUpClone: false,
					anchorNav: true,
					autoHeight: false,
					stickUpOffset: '1px',
					responsive: {
						0: {
							layout: 'rd-navbar-fixed',
							deviceLayout: 'rd-navbar-fixed',
							focusOnHover: 'ontouchstart' in window,
							stickUp: false
						},
						992: {
							layout: 'rd-navbar-fixed',
							deviceLayout: 'rd-navbar-fixed',
							focusOnHover: 'ontouchstart' in window,
							stickUp: false
						},
						1200: {
							layout: 'rd-navbar-fullwidth',
							deviceLayout: 'rd-navbar-fullwidth',
							stickUp: true,
							stickUpOffset: '1px'
						}
					},
					callbacks: {
						onStuck: function () {
							document.documentElement.classList.add( 'rd-navbar-stuck' );
						},
						onUnstuck: function () {
							document.documentElement.classList.remove( 'rd-navbar-stuck' );
						},
						onDropdownToggle: function () {
							if ( this.classList.contains( 'opened' ) ) {
								this.parentElement.classList.add( 'overlaid' );
							} else {
								this.parentElement.classList.remove( 'overlaid' );
							}
						},
						onDropdownClose: function () {
							this.parentElement.classList.remove( 'overlaid' );
						}
					}
				},
				xMode = {
					stickUpClone: false,
					anchorNav: false,
					responsive: {
						0: {
							stickUp: false,
							stickUpClone: false
						},
						992: {
							stickUp: false,
							stickUpClone: false
						},
						1200: {
							stickUp: false,
							stickUpClone: false
						}
					},
					callbacks: {
						onDropdownOver: function () { return false; }
					}
				},
				navbar = node.RDNavbar = new RDNavbar( node, Util.merge( window.xMode ? [ defaults, params, xMode ] : [ defaults, params ] ) );

			if ( backButtons.length ) {
				backButtons.forEach( function ( btn ) {
					btn.addEventListener( 'click', function () {
						let
							submenu = this.closest( '.rd-navbar-submenu' ),
							parentmenu = submenu.parentElement;

						navbar.dropdownToggle.call( submenu, navbar );
					});
				});
			}
		})
	}
};

components.slick = {
	selector: '.slick-slider',
	styles: './components/slick/slick.css',
	script: [
		'./components/jquery/jquery.min.js',
		'./components/slick/slick.min.js',
		'./components/util/util.min.js'
	],
	init: function ( nodes ) {
		nodes.forEach( function ( node ) {
			let
				defaults = {
					autoplay:  true,
					prevArrow: '<button type="button" class="slick-prev"></button>',
					nextArrow: '<button type="button" class="slick-next"></button>'
				},
				breakpoint = { xs: 480, sm: 576, md: 768, lg: 992, xl: 1200, xxl: 1600 }, // slick slider uses desktop first principle
				responsive = [],
				params;

			// Making responsive parameters
			for ( let key in breakpoint ) {
				if ( node.hasAttribute( 'data-slick-' + key ) ) {
					responsive.push({
						breakpoint: breakpoint[ key ],
						settings: parseJSON( node.getAttribute( 'data-slick-' + key ) )
					});
				}
			}

			params = {
				responsive: responsive
			};

			let tmp = Util.merge( [ defaults, params ] );

			$( node ).slick( tmp );

			// Filtering
			let links = document.querySelectorAll( '.slick-filter-link' );
			links.forEach( function( element ) {
				element.addEventListener( 'click', function () {
					let filter = element.getAttribute( 'data-filter' );
					$( node ).slick( 'slickUnfilter' );
					if( filter !== '*' ) {
						$( node ).slick( 'slickFilter', '[data-category="' + filter + '"]' );
					}
				});
			});
		});
	}
};

components.swiper = {
	selector: '.swiper-container',
	styles: [
		'./components/animate/animate.css',
		'./components/swiper/swiper.css'
	],
	script: [
		'./components/swiper/swiper.min.js',
		'./components/swiper/swiper-progress-circle.min.js',
		'./components/util/util.min.js'
	],
	init: function ( nodes ) {
		nodes.forEach( function ( node ) {

			// Pagination decimal leading zero
			function pad( number, length ) {
				let str = '' + number;
				while ( str.length < length ) {
					str = '0' + str;
				}

				return str;
			}

			/**
			 * Update of secondary numeric pagination
			 * @this {object}  - swiper instance
			 */
			function updSwiperNumericPagination() {
				if ( this.el.querySelector( '.swiper-counter' ) ) {
					this.el.querySelector('.swiper-counter')
							.innerHTML = '<span class="swiper-counter-count">' +  formatIndex((this.realIndex + 1)) + '</span><span class="swiper-counter-divider"></span><span class="swiper-counter-total">' + formatIndex((this.slides.length)) + '</span>';
				}
			}
			function formatIndex(index) {
				return index < 10 ? '0' + index : index;
			}

			let
				slides = node.querySelectorAll( '.swiper-slide[data-slide-bg]' ),
				animate = node.querySelectorAll( '.swiper-wrapper [data-caption-animate]' ),
				videos = node.querySelectorAll( '.swiper-wrapper video' ),
				pagOrdered = node.querySelector( '.swiper-pagination[data-pagination-ordered]' ),
				pagProgress = node.querySelector( '.swiper-pagination[data-pagination-progress]' ),
				progress,
				timer,
				params = merge({
					speed: 500,
					loop: true,
					autoHeight: false,
					pagination: {
						el: '.swiper-pagination',
						clickable: true,
						renderBullet: function ( index, className ) {
							return (
								'<span class="' + className + '">' +
								( pagOrdered ? pad( ( index + 1 ), 2 ) : '' ) +
								( pagProgress ?
									'<svg class="swiper-progress" x="0px" y="0px" width="100" height="100" viewbox="0 0 100 100">' +
									'<circle class="swiper-progress-bg" cx="50" cy="50" r="50"></circle>' +
									'<circle class="swiper-progress-dot" cx="50" cy="50" r="14"></circle>' +
									'<circle class="clipped" cx="50" cy="50" r="48"></circle>' +
									'</svg>' : '' ) +
								'</span>'
							)
						}
					},
					navigation: {
						nextEl: '.swiper-button-next',
						prevEl: '.swiper-button-prev'
					},
					scrollbar: {
						el: '.swiper-scrollbar'
					},
					autoplay: {
						delay: 5000,
						disableOnInteraction: false
					},
					on: {

						init: updSwiperNumericPagination,
						slideChange: updSwiperNumericPagination,
						paginationUpdate: function() {
							if( pagProgress ) {
								let
									bullets = pagProgress.querySelectorAll( '.swiper-pagination-bullet' ),
									bulletActive = pagProgress.querySelector( '.swiper-pagination-bullet-active .swiper-progress' );

								progress = new aProgressCircle({ node: bulletActive });
								timer = new VirtualTimer({ onTick: function () {
									progress.render( this.progress / this.duration * 360 );
								}});

								timer.reset();
								timer.duration = this.originalParams.autoplay.delay - 100;
								timer.start();

								bullets.forEach( function( bullet ) {
									bullet.addEventListener( 'click', function() {
										timer.stop();
									} )
								} );
							}
						},
						sliderMove: function() {
							timer.stop();
							timer.reset();
						}
					}
				}, parseJSON( node.getAttribute( 'data-swiper' ) ) );

			// Specific params for Novi builder
			if ( window.xMode ) {
				params = merge( params, {
					autoplay: false,
					loop: false,
					simulateTouch: false
				});
			}

			// Set background image for slides with `data-slide-bg` attribute
			slides.forEach( function ( slide ) {
				slide.style.backgroundImage = 'url('+ slide.getAttribute( 'data-slide-bg' ) +')';
			});

			// Animate captions with `data-caption-animate` attribute
			if ( animate.length ) {
				if ( !params.on ) params.on = {};
				params.on.transitionEnd = function () {
					let
						active = this.wrapperEl.children[ this.activeIndex ],
						prev = this.wrapperEl.children[ this.previousIndex ];

					active.querySelectorAll( '[data-caption-animate]' ).forEach( function ( node ) {
						node.classList.add( node.getAttribute( 'data-caption-animate' ) );
						node.classList.add( 'animated' );
					});

					prev.querySelectorAll( '[data-caption-animate]' ).forEach( function ( node ) {
						node.classList.remove( node.getAttribute( 'data-caption-animate' ) );
						node.classList.remove( 'animated' );
					})
				}
			}

			// Stop video on inactive slides
			if ( videos.length ) {
				if ( !params.on ) params.on = {};
				params.on.transitionStart = function () {
					let
						active = this.wrapperEl.children[ this.activeIndex ],
						prev = this.wrapperEl.children[ this.previousIndex ];

					active.querySelectorAll( 'video' ).forEach( function ( video ) { if ( video.paused ) video.play(); });
					prev.querySelectorAll( 'video' ).forEach( function ( video ) { if ( !video.paused ) video.pause(); })
				}
			}

			// Initialization if there are related swipers
			if ( params.thumbs && params.thumbs.swiper ) {
				let target = document.querySelector( params.thumbs.swiper );

				if ( !target.swiper ) {
					target.addEventListener( 'swiper:ready', function () {
						params.thumbs.swiper = target.swiper;
						new Swiper( node, params );
						node.dispatchEvent( new CustomEvent( 'swiper:ready' ) );
					});
				} else {
					params.thumbs.swiper = target.swiper;
					new Swiper( node, params );
					node.dispatchEvent( new CustomEvent( 'swiper:ready' ) );
				}
			} else {
				new Swiper( node, params );
				node.dispatchEvent( new CustomEvent( 'swiper:ready' ) );
			}
		});
	}
};

components.regula = {
	selector: '[data-constraints]',
	styles: './components/regula/regula.css',
	script: [
		'./components/jquery/jquery.min.js',
		'./components/regula/regula.min.js'
	],
	init: function ( nodes ) {
		let elements = $( nodes );

		// Custom validator - phone number
		regula.custom({
			name: 'PhoneNumber',
			defaultMessage: 'Invalid phone number format',
			validator: function() {
				if ( this.value === '' ) return true;
				else return /^(\+\d)?[0-9\-\(\) ]{5,}$/i.test( this.value );
			}
		});

		for (let i = 0; i < elements.length; i++) {
			let o = $(elements[i]), v;
			o.addClass("form-control-has-validation").after("<span class='form-validation'></span>");
			v = o.parent().find(".form-validation");
			if (v.is(":last-child")) o.addClass("form-control-last-child");
		}

		elements.on('input change propertychange blur', function (e) {
			let $this = $(this), results;

			if (e.type !== "blur") if (!$this.parent().hasClass("has-error")) return;
			if ($this.parents('.rd-mailform').hasClass('success')) return;

			if (( results = $this.regula('validate') ).length) {
				for (let i = 0; i < results.length; i++) {
					$this.siblings(".form-validation").text(results[i].message).parent().addClass("has-error");
				}
			} else {
				$this.siblings(".form-validation").text("").parent().removeClass("has-error")
			}
		}).regula('bind');

		let regularConstraintsMessages = [
			{
				type: regula.Constraint.Required,
				newMessage: "The text field is required."
			},
			{
				type: regula.Constraint.Email,
				newMessage: "The email is not a valid email."
			},
			{
				type: regula.Constraint.Numeric,
				newMessage: "Only numbers are required"
			},
			{
				type: regula.Constraint.Selected,
				newMessage: "Please choose an option."
			}
		];


		for (let i = 0; i < regularConstraintsMessages.length; i++) {
			let regularConstraint = regularConstraintsMessages[i];

			regula.override({
				constraintType: regularConstraint.type,
				defaultMessage: regularConstraint.newMessage
			});
		}
	}
};

components.tooltip = {
	selector: '[data-toggle="tooltip"]',
	styles: './components/tooltip/tooltip.css',
	script: [
		'./components/jquery/jquery.min.js',
		'./components/bootstrap/js/popper.min.js',
		'./components/bootstrap/js/bootstrap.min.js'
	],
	init: function( nodes ) {
		nodes.forEach( function ( node ) {
			$( node ).tooltip();
		} );
	}
};

components.preloader = {
	selector: '.preloader',
	styles:   './components/preloader/preloader.css'
};

components.toTop = {
	selector: 'html',
	styles: './components/to-top/to-top.css',
	script: './components/jquery/jquery.min.js',
	init: function () {
		if ( !window.xMode ) {
			let node = document.createElement( 'div' );
			node.className = 'to-top mdi-chevron-up';
			document.body.appendChild( node );

			node.addEventListener( 'mousedown', function () {
				this.classList.add( 'active' );

				$( 'html, body' ).stop().animate( { scrollTop:0 }, 500, 'swing', (function () {
					this.classList.remove( 'active' );
				}).bind( this ));
			});

			document.addEventListener( 'scroll', function () {
				if ( window.scrollY > window.innerHeight ) node.classList.add( 'show' );
				else node.classList.remove( 'show' );
			});
		}
	}
};

/**
 * Wrapper to eliminate json errors
 * @param {string} str - JSON string
 * @returns {object} - parsed or empty object
 */
function parseJSON ( str ) {
	try {
		if ( str )  return JSON.parse( str );
		else return {};
	} catch ( error ) {
		console.warn( error );
		return {};
	}
}

/**
 * Get tag of passed data
 * @param {*} data
 * @return {string}
 */
function objectTag ( data ) {
	return Object.prototype.toString.call( data ).slice( 8, -1 );
}

/**
 * Merging of two objects
 * @param {Object} source
 * @param {Object} merged
 * @return {Object}
 */
function merge( source, merged ) {
	for ( let key in merged ) {
		let tag = objectTag( merged[ key ] );

		if ( tag === 'Object' ) {
			if ( typeof( source[ key ] ) !== 'object' ) source[ key ] = {};
			source[ key ] = merge( source[ key ], merged[ key ] );
		} else if ( tag !== 'Null' ) {
			source[ key ] = merged[ key ];
		}
	}

	return source;
}

/**
 * Strict merging of two objects. Merged only parameters from the original object and with the same data type. Merge only simple data types, arrays and objects.
 * @param source
 * @param merged
 * @return {object}
 */
function strictMerge( source, merged ) {
	for ( let key in source ) {
		let
			sTag = objectTag( source[ key ] ),
			mTag = objectTag( merged[ key ] );

		if ( [ 'Object', 'Array', 'Number', 'String', 'Boolean', 'Null', 'Undefined' ].indexOf( sTag ) > -1 ) {
			if ( sTag === 'Object' && sTag === mTag ) {
				source[ key ] = strictMerge( source[ key ], merged[ key ] );
			} else if ( mTag !== 'Undefined' && ( sTag === 'Undefined' || sTag === 'Null' || sTag === mTag ) ) {
				source[ key ] = merged[ key ];
			}
		}
	}

	return source;
}


// Main
window.addEventListener( 'load', function () {
	new ZemezCore({
		debug: true,
		components: components,
		observeDOM: window.xMode,
		IEHandler: function ( version ) {
			document.documentElement.classList.add( 'ie-'+ version );
		}
	});
});
