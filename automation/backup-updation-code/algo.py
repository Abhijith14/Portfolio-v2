def update_badges_by_latest_last(html_str, code):
    latest_count = html_str.count('badges_items')
    start = html_str.index('<!-- badges_end -->')

    new_badge = '''
    <!-- badges_items '''+ str(latest_count + 1) +''' -->
    ''' + code


    return html_str[:start] + new_badge + html_str[start:]


def update_badges_by_position(html_str, code, position):
    latest_count = html_str.count('badges_items')

    if position > latest_count or position <= 0:
        return update_badges_by_latest_last(html_str, code)
        
    start = html_str.index('<!-- badges_items '+ str(position) +' -->')
    
    for i in range(latest_count, position-1, -1):
        curr_str = '''<!-- badges_items '''+ str(i) +''' -->'''
        new_str = '''<!-- badges_items '''+ str(i+1) +''' -->'''
        
        html_str = html_str.replace(curr_str, new_str)  
    
    new_badge = '''
    <!-- badges_items '''+ str(position) +''' -->
    ''' + code

    return html_str[:start] + new_badge + html_str[start:]


def update_badges(html_str, image, title, desc, date, position=-1):

    new_badge_code = '''
                    <!-- Pricing-->
                        <article class="pricing pricing-primary block block-sm block-center" data-animate='{"class":"fadeInUp"}'>
                        <div class="pricing-body">
                            <a href="'''+str(image)+'''" target="_blank"><img src="'''+str(image)+'''" alt="" width="100%" height="100%" loading="lazy"></a>
                            <div class="pricing-divider">
                            <hr class="divider">
                            </div>
                            <div class="pricing-btn">
                                    <center><b>'''+str(title)+'''</b></center>
                            '''+str(desc)+'''<br>'''+str(date)+'''
                            </div>
                        </div>
                        </article>
    '''

    if position >= 0:
        return update_badges_by_position(html_str, new_badge_code, position)
    else:
        return update_badges_by_latest_last(html_str, new_badge_code)


def update_achievements_by_latest_last(html_str, code):
    latest_count = html_str.count('achievements_items')
    start = html_str.index('<!-- achievements_end -->')

    new_achievement = '''
    <!-- achievements_items '''+ str(latest_count + 1) +''' -->
    ''' + code


    return html_str[:start] + new_achievement + html_str[start:]


def update_achievements(html_str, image, title, desc, date, position=-1):
    new_achievements_code=  '''
    <!-- Pricing -->

    <article class="pricing pricing-primary block block-sm block-center" data-animate='{"class":"fadeInUp"}'>
                      <div class="pricing-body">
                        <a href="'''+ image +'''" target="_blank"><img src="'''+ image +'''" alt="" width="100%" height="100%" loading="lazy"></a>
                        <div class="pricing-divider">
                          <hr class="divider">
                        </div>
                        <div class="pricing-btn">
                        	<center><b>'''+ title +'''</b></center>
                          '''+ desc +'''<br>'''+ date +'''
                        </div>
                      </div>
                    </article>
    '''

    if position >= 0:
        pass
        # return update_achievements_by_position(html_str, new_achievements_code, position)
    else:
        return update_achievements_by_latest_last(html_str, new_achievements_code)


def save(html_str):
    f_write = open("./index.html", "w")
    f_write.write(html_str)
    f_write.close()

