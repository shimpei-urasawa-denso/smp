try
=====


.. req:: Basic need example
    :id: BASIC_EXAMPLE
    :status: open

    A basic example of a need item.


.. req:: tekitou
    :status: open

    hogehoge


.. tutorial-project:: Our new car
    :id: T_CAR
    :status: in progress
    :tags: tutorial
    :layout: clean_l
    :image: _static/car.png
    :collapse: true

    Presenting the “TeenTrek,” an autonomous driving car tailored for teenagers without a driving license.
    Equipped with advanced AI navigation and safety protocols, it ensures effortless and secure transportation.
    The interior boasts entertainment systems, study areas, and social hubs, catering to teen preferences.
    The TeenTrek fosters independence while prioritizing safety and convenience for young passengers.


The project is described in more detail in :need:`T_CAR`.

The project is described in more detail in :need:`[[title]] <T_CAR>`.

.. req:: Safety Features
   :id: T_SAFE
   :tags: tutorial
   :tutorial_required_by: T_CAR

   The car must include advanced safety features such as automatic braking, collision avoidance systems, and adaptive cruise control to ensure the safety of teenage drivers.

.. req:: Connectivity and Entertainment
   :id: T_CONNECT
   :tags: tutorial
   :tutorial_required_by: T_CAR

   The car should be equipped with built-in Wi-Fi, Bluetooth connectivity, and compatibility with smartphone integration systems to enable seamless communication and entertainment for teenagers on the go.


.. spec:: Implement RADAR system
   :id: T_RADAR
   :tags: tutorial
   :tutorial_specifies_by: T_SAFE

   The RADAR sensor software for the car must accurately detect and track surrounding objects
   within a specified range. It should employ signal processing algorithms to filter out noise
   nd interference, ensuring reliable object detection in various weather and road conditions.
   The software should integrate seamlessly with the car's control system, providing real-time
   data on detected objects to enable collision avoidance and adaptive cruise control functionalities.
   Additionally, it should adhere to industry standards for safety and reliability, with robust
   error handling mechanisms in place.


.. spec:: Implement distant detection
   :id: T_DIST
   :status: open
   :tags: tutorial
   :tutorial_specifies_by: T_SAFE

   Software Specification for Distance Detection Algorithm.


.. req:: needextend Example 1
   :id: ETEST001
   :status: open
   :author: Foo
   :tags: tag_1, tag_2

   This requirement got modified.

..    | Status was **open**, now it is :ndf:`copy('status')`.
..    | Also author got changed from **Foo** to :ndf:`copy('author')`.
..    | And a tag was added.
..    | Finally all links got removed.

.. req:: needextend Example 2
   :id: ETEST002
   :tags: extend_example
   :status: open

   Contents

.. needextend:: ETEST001
   :status: closed
   :+author: and me

.. needextend:: <ETEST001>
   :+tags: new_tag

.. needextend:: id == "ETEST002"
   :status: New status

.. needextend:: ""extend_example" in tags"
   :+tags: other


.. needlist::
    :tags: tutorial
    :sort_by: id
    :show_status:


.. needtable::
    :tags: tutorial
    :sort: id
    :columns: id, type, title, status
    :style: table


.. needtable::
    :tags: tutorial
    :sort: id
    :columns: id,type,title,status
    :style: datatable


.. needflow:: Engineering plan to develop a car
    :alt: Engineering plan to develop a car
    :root_id: T_CAR
    


    .. :config: lefttoright
    .. :show_link_names:


    .. :border_color:
    ..     [status == 'open']:#FF0000,
    ..     [status == 'in progress']:#0000FF,
    ..     [status == 'closed']:#00FF00
